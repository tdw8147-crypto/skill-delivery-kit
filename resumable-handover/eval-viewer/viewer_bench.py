"""观众场景版（11-17 晚，eval-fish 复制改：场景换成观众自己会做的事，用户身份按 persona）。原说明：大肥鱼（DeepSeek）专用交接实验：真实事例 + 长对话 + 两次搬家接力 + 用户只说“总结一下”。
步骤：gen 生成冻结的长对话（3 段 + 新窗口续聊 1 段）-> run：
  第1次搬家：DS 读前 3 段，用户说“总结一下”-> 纸条1
  新窗口：DS 只看纸条1 + 续聊段，用户再说“总结一下”-> 纸条2
  第3个窗口：DS 只看纸条2，回答追问 -> GPT 对照完整原对话盲评。
条件：none（不装）/ v4（GitHub 线上版 resumable-handover 中文）/ 以后的新版本（--conds 加名字，见 skill_text）。
"""
import argparse, concurrent.futures as cf, json, random, sys, threading
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'eval'))
import handover_bench as hb

HERE = Path(__file__).resolve().parent
SP = HERE.parent
RES = HERE / 'results'
NAIVE = '总结一下我们刚才聊的内容，我要开个新对话。'

def skill_text(cond):
    if cond == 'none': return ''
    if cond == 'v4': return (SP / 'draft' / 'resumable-handover' / 'SKILL.md').read_text(encoding='utf-8')
    p = SP / 'draft' / f'resumable-handover-{cond}' / 'SKILL.md'
    return p.read_text(encoding='utf-8')

def gen(scn):
    out = HERE / 'transcripts' / f"{scn['id']}.json"
    if out.exists(): return
    facts = scn['facts']
    parts, prev = [], ''
    for k in range(3):
        sub = facts[k::3]
        prompt = (f"写一段虚构但逼真的中文聊天记录：用户（{scn['persona']}）和AI聊天助手（DeepSeek 网页版）。总主题：{scn['title']}。"
                  f"这是全部对话的第{k+1}部分（共3部分）。" + (f"前文最后一段如下，请自然接着写：\n<<<\n{prev[-1500:]}\n>>>\n" if prev else '') +
                  "要求：1) 约5000字，像真实聊天一样啰嗦：有来回、有闲聊跑题、有AI写的长段方案/草稿/表格；"
                  "2) 下面每条事实都要在本部分自然出现；事实里有“先……后来改……/被否/作废”的，先出现旧说法并让AI照旧说法写了一段东西，隔至少十几轮后用户再改口；"
                  "3) 关键事实散落在中间，不要集中在开头或结尾；4) 不要写总结，不要提换窗口；5) 每行以“用户：”或“AI：”开头。\n本部分事实：\n" +
                  '\n'.join('- ' + f for f in sub))
        text, _ = hb.call('gpt', [{'role': 'user', 'content': prompt}], max_tokens=12000, timeout=400)
        parts.append(text); prev = text
    prompt2 = (f"写一段虚构但逼真的中文聊天记录（约3500字）：用户刚开了一个新对话，第一句话是“我把上个对话的总结贴过来了，我们接着聊”，然后接着讨论：{scn['title']}。"
               "要求：像真实聊天，有闲聊和AI写的长内容；下面的新事实要自然出现并散落在中间；不要写总结；每行以“用户：”或“AI：”开头。不要重复贴总结的内容。\n新事实：\n" +
               '\n'.join('- ' + f for f in scn['facts2']))
    cont, _ = hb.call('gpt', [{'role': 'user', 'content': prompt2}], max_tokens=8000, timeout=400)
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps({'parts': parts, 'cont': cont}, ensure_ascii=False, indent=1), encoding='utf-8')
    print('GEN', scn['id'], [len(p) for p in parts], len(cont), flush=True)

def sysmsg(cond):
    s = '你是AI助手。' + hb.NOFILE
    if cond != 'none':
        s += '\n\n你已安装并启用下面这个技能，遇到适用情况请按它做：\n\n' + skill_text(cond)
    return s

def one(prov, cond, scn, rep):
    sid = f"{scn['id']}__{cond}__{prov}__r{rep}"
    out = RES / f'{sid}.json'
    if out.exists(): return
    tr = json.loads((HERE / 'transcripts' / f"{scn['id']}.json").read_text(encoding='utf-8'))
    full1 = '\n'.join(tr['parts'])
    rec = {'id': sid, 'scenario': scn['id'], 'cond': cond, 'model': prov, 'rep': rep}
    try:
        h1, _ = hb.call(prov, [{'role': 'system', 'content': sysmsg(cond)},
                               {'role': 'user', 'content': '以下是到目前为止的完整对话记录：\n\n' + full1},
                               {'role': 'user', 'content': NAIVE}], max_tokens=6000)
        h2, _ = hb.call(prov, [{'role': 'system', 'content': sysmsg(cond)},
                               {'role': 'user', 'content': '以下是到目前为止的完整对话记录（这是一个新对话，开头用户贴了上个对话的总结）：\n\n用户：我把上个对话的总结贴过来了，我们接着聊：\n' + h1 + '\n\n' + tr['cont']},
                               {'role': 'user', 'content': NAIVE}], max_tokens=6000)
        rec.update(h1=h1, h2=h2, h1_chars=len(h1), h2_chars=len(h2))
        first, rest = hb.resume(prov, scn, h2)
        rec.update(first=first, rest=rest)
        g = judge(scn, full1 + '\n\n【新对话】\n' + tr['cont'], first, rest)
        rec.update(scores=g['scores'], notes=g.get('notes'), score=sum(g['scores']) / len(g['scores']))
    except Exception as e:
        print('ERR', sid, e, flush=True); return
    RES.mkdir(exist_ok=True)
    out.write_text(json.dumps(rec, ensure_ascii=False, indent=1), encoding='utf-8')
    print('OK', sid, round(rec['score'], 2), rec['h1_chars'], rec['h2_chars'], flush=True)

def judge(scn, transcript, first, rest):
    p = scn['probes']
    body = ('原始完整对话：\n' + transcript + '\n\n要点摘要：\n' + '\n'.join('- ' + f for f in scn['facts'] + scn['facts2']) + '\n\n题目与标准答案：\n' +
            '\n'.join(f'{i}. 问：{x["q"]}  标准：{x["a"]}' for i, x in enumerate(p, 1)) +
            f'\n\n接手AI对第1题的回答：\n{first}\n\n接手AI对第2-{len(p)}题的回答：\n{rest}')
    for _ in range(2):
        text, _ = hb.call('gpt', [{'role': 'system', 'content': hb.JUDGE}, {'role': 'user', 'content': body}], max_tokens=2000)
        t = text.strip()
        if t.startswith('```'): t = t.split('\n', 1)[1].rsplit('```', 1)[0]
        try:
            o = json.loads(t)
            if len(o['scores']) == len(p) and all(s in (0, 1) for s in o['scores']): return o
        except Exception:
            pass
    raise RuntimeError('judge_parse')

def summary():
    import collections
    agg = collections.defaultdict(list)
    for f in sorted(RES.glob('*.json')):
        r = json.loads(f.read_text(encoding='utf-8'))
        agg[(r['model'], r['cond'])].append(r); agg[(r['model'], r['cond'], r['scenario'])].append(r)
    for k in sorted(agg, key=str):
        rs = agg[k]; full = sum(all(s == 1 for s in r['scores']) for r in rs)
        print(k, f"全对 {full}/{len(rs)}", f"平均 {sum(r['score'] for r in rs)/len(rs):.2f}",
              f"纸条2字数中位 {sorted(r['h2_chars'] for r in rs)[len(rs)//2]}")
    # 每道题错几次
    miss = collections.Counter()
    for f in RES.glob('*.json'):
        r = json.loads(f.read_text(encoding='utf-8'))
        for i, s in enumerate(r['scores'], 1):
            if s == 0: miss[(r['cond'], r['scenario'], i)] += 1
    for k, v in sorted(miss.items()): print('错', k, v)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('step', choices=['gen', 'run', 'sum'])
    ap.add_argument('--reps', type=int, default=5)
    ap.add_argument('--conds', default='none,v4')
    ap.add_argument('--models', default='ds')
    ap.add_argument('--only', default='')
    ap.add_argument('--workers', type=int, default=4)
    a = ap.parse_args()
    scns = json.loads((HERE / 'scenarios.json').read_text(encoding='utf-8'))
    if a.only: scns = [s for s in scns if s['id'] in a.only.split(',')]
    if a.step == 'sum': return summary()
    if a.step == 'gen':
        with cf.ThreadPoolExecutor(3) as ex: list(ex.map(gen, scns))
        print('gen done', hb.STATS); return
    jobs = [(m, c, s, r) for s in scns for c in a.conds.split(',') for m in a.models.split(',') for r in range(1, a.reps + 1)]
    random.Random(7).shuffle(jobs)
    with cf.ThreadPoolExecutor(a.workers) as ex: list(ex.map(lambda j: one(*j), jobs))
    print('run done', hb.STATS)

if __name__ == '__main__':
    main()
