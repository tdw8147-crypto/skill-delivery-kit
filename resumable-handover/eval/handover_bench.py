"""换窗口交接对比：none / ours / pwf，GPT + DeepSeek。只用标准库。
步骤：gen 生成冻结的长对话 -> run 写交接 -> 新窗口只看交接答探针 -> 盲评。
"""
import argparse, concurrent.futures as cf, json, random, sys, threading, time, hashlib, re
from pathlib import Path
from fast_client import lookup_provider, default_transport  # our gateway; replace with your own client

HERE = Path(__file__).resolve().parent
PROJ = HERE.parents[1]
MODELS = {'gpt': ('gpt-6.1-terra', 'provider-a'), 'ds': ('deepseek-v4.1-flash', 'provider-b')}
PWF = HERE / 'skills' / 'pwf'
LOCK = threading.Lock()
CREDS = {}
STATS = {'calls': 0, 'fail': 0}

def call(prov, messages, max_tokens=3000, timeout=180):
    with LOCK:
        if prov not in CREDS: CREDS[prov] = lookup_provider(MODELS[prov][1])
        STATS['calls'] += 1
    payload = {'model': MODELS[prov][0], 'messages': messages, 'max_tokens': max_tokens}
    if prov == 'gpt': payload['reasoning_effort'] = 'low'
    else: payload['thinking'] = {'type': 'disabled'}
    for attempt in range(2):
        try:
            status, data = default_transport(provider=CREDS[prov], payload=payload, timeout=timeout)
            if status == 200:
                c = data['choices'][0]
                text = c['message'].get('content') or ''
                if text.strip():
                    return text, (data.get('usage') or {})
        except Exception:
            pass
        with LOCK: STATS['fail'] += 1
        time.sleep(5)
    raise RuntimeError('call_failed')

def skill_text(cond):
    if cond == 'none': return ''
    if cond == 'ours':
        return (HERE / 'skills' / 'v3-compact.zh.md').read_text(encoding='utf-8')
    if cond == 'v4en':
        return (HERE.parent / 'SKILL.md').read_text(encoding='utf-8')
    if cond == 'live':
        return (HERE / 'skills' / 'previous.zh.md').read_text(encoding='utf-8')
    if cond == 'v4':
        return (HERE.parent / 'SKILL.zh.md').read_text(encoding='utf-8')
    if cond == 'pwf':
        s = (PWF / 'i18n' / 'planning-with-files-zh' / 'SKILL.md').read_text(encoding='utf-8')
        for t in ('task_plan', 'findings', 'progress'):
            s += f'\n\n=== 模板 templates/{t}.md ===\n' + (PWF / 'planning-with-files' / 'templates' / f'{t}.md').read_text(encoding='utf-8')
        return s
    raise ValueError(cond)

TRIGGER = {
    'chat': '这个对话太长了，马上到上限。帮我写一份东西，我复制到新对话里接着聊，新对话里的你只能看到这份东西。',
    'agent': '上下文快满了，马上要清空重开。请写好接续用的内容，新会话只能看到你这次的输出，看不到之前任何记录。',
}
NAIVE = {'chat': '总结一下我们刚才聊的内容，我要开个新对话。', 'agent': '总结一下目前的进度。'}
RES = 'results'
NOFILE = '（本环境不能写磁盘也不能调用工具。如果你的方法需要写文件，请把每个文件的完整内容直接输出在回复里。）'

def gen(scn):
    out = HERE / 'transcripts' / f"{scn['id']}.txt"
    if out.exists(): return
    who = '用户和AI聊天助手（网页版）' if scn['kind'] == 'chat' else '用户和编程/操作类AI Agent（Agent 会调用工具，工具输出用【工具】开头）'
    prompt = (f"写一段虚构的、逼真的中文长对话记录，{who}，主题：{scn['title']}。\n"
              "要求：1) 4500-6000字，像真实聊天一样啰嗦，有来回、有闲聊、有AI写的长段内容；"
              "2) 下面每条事实都必须在对话中自然出现，涉及‘改了/作废/取消/先别’的，要先出现旧说法，隔几轮后再由用户改口；"
              "3) 关键事实不要集中在结尾，要散落在中间；4) 对话在用户说要换窗口之前停止，不要写总结；"
              "5) 格式每行以‘用户：’‘AI：’或‘【工具】’开头。\n事实：\n" + '\n'.join('- ' + f for f in scn['facts']))
    text, _ = call('gpt', [{'role': 'user', 'content': prompt}], max_tokens=12000, timeout=300)
    out.parent.mkdir(exist_ok=True)
    out.write_text(text, encoding='utf-8')

def write_handover(prov, cond, scn, transcript):
    sys_msg = '你是AI助手。' + NOFILE
    if cond != 'none':
        sys_msg += '\n\n你已安装并启用下面这个技能，遇到适用情况请按它做：\n\n' + skill_text(cond)
    msgs = [{'role': 'system', 'content': sys_msg},
            {'role': 'user', 'content': '以下是到目前为止的完整对话记录：\n\n' + transcript},
            {'role': 'user', 'content': (NAIVE if RES != 'results' else TRIGGER)[scn['kind']]}]
    return call(prov, msgs, max_tokens=6000)

def resume(prov, scn, handover):
    base = ('你是接手的AI助手，是一个全新的窗口，之前的对话你看不到。用户贴给你下面这份交接内容：\n\n'
            '<<<交接开始>>>\n' + handover + '\n<<<交接结束>>>')
    p = scn['probes']
    first, _ = call(prov, [{'role': 'system', 'content': base},
                           {'role': 'user', 'content': p[0]['q'] + '（直接说你要做的事，简短）'}], max_tokens=1500)
    rest_q = '\n'.join(f'{i}. {x["q"]}' for i, x in enumerate(p[1:], 2))
    rest, _ = call(prov, [{'role': 'system', 'content': base},
                          {'role': 'user', 'content': '我接着问你几件事，按编号逐条简短回答：\n' + rest_q}], max_tokens=2500)
    return first, rest

JUDGE = ('你是盲评员。下面是原始完整对话（唯一事实来源）、要点摘要、探针问题和标准答案，以及接手AI的回答（接手AI只看过一份交接，没看过原对话）。'
         '逐题判断：回答抓住了标准答案的核心要点就给1；答错、说不知道、与原对话最终状态矛盾、或擅自要做被禁止/取消/未决的事给0。'
         '原对话里出现过的额外细节不算编造；只有原对话里没有且影响结论的内容才算编造。若原对话最终状态与标准答案不一致，以原对话为准。'
         '附加说明、谨慎提醒不扣分。'
         '只输出JSON：{"scores":[0或1,...],"notes":["每题一句理由",...]}，scores 长度必须等于题数。')

def judge(scn, first, rest):
    p = scn['probes']
    tr = (HERE / 'transcripts' / f"{scn['id']}.txt").read_text(encoding='utf-8')
    body = ('原始完整对话：\n' + tr + '\n\n要点摘要：\n' + '\n'.join('- ' + f for f in scn['facts']) + '\n\n题目与标准答案：\n' +
            '\n'.join(f'{i}. 问：{x["q"]}  标准：{x["a"]}' for i, x in enumerate(p, 1)) +
            f'\n\n接手AI对第1题的回答：\n{first}\n\n接手AI对第2-{len(p)}题的回答：\n{rest}')
    for _ in range(2):
        text, _ = call('gpt', [{'role': 'system', 'content': JUDGE}, {'role': 'user', 'content': body}], max_tokens=2000)
        t = text.strip()
        if t.startswith('```'): t = t.split('\n', 1)[1].rsplit('```', 1)[0]
        try:
            o = json.loads(t)
            if len(o['scores']) == len(p) and all(s in (0, 1) for s in o['scores']): return o
        except Exception:
            pass
    raise RuntimeError('judge_parse')

def one(prov, cond, scn, rep):
    sid = f"{scn['id']}__{cond}__{prov}__r{rep}"
    out = HERE / RES / f'{sid}.json'
    if out.exists(): return json.loads(out.read_text(encoding='utf-8'))
    tr = (HERE / 'transcripts' / f"{scn['id']}.txt").read_text(encoding='utf-8')
    rec = {'id': sid, 'scenario': scn['id'], 'kind': scn['kind'], 'cond': cond, 'model': prov, 'rep': rep}
    try:
        h, usage = write_handover(prov, cond, scn, tr)
        rec.update(handover=h, handover_chars=len(h), writer_usage=usage)
        first, rest = resume(prov, scn, h)
        rec.update(first=first, rest=rest)
        g = judge(scn, first, rest)
        rec.update(scores=g['scores'], notes=g.get('notes'), score=sum(g['scores']) / len(g['scores']))
    except Exception as e:
        rec['error'] = str(e)
        print('ERR', sid, e, flush=True)
        return rec
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps(rec, ensure_ascii=False, indent=2), encoding='utf-8')
    print('OK', sid, round(rec['score'], 2), rec['handover_chars'], flush=True)
    return rec

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('step', choices=['gen', 'run', 'rejudge'])
    ap.add_argument('--reps', type=int, default=2)
    ap.add_argument('--only', default='')
    ap.add_argument('--workers', type=int, default=4)
    ap.add_argument('--naive', action='store_true')
    ap.add_argument('--conds', default='none,ours,pwf')
    a = ap.parse_args()
    global RES
    if a.naive: RES = 'results_naive'
    scns = json.loads((HERE / 'scenarios.json').read_text(encoding='utf-8'))
    if a.only: scns = [s for s in scns if s['id'] in a.only.split(',')]
    if a.step == 'gen':
        with cf.ThreadPoolExecutor(a.workers) as ex: list(ex.map(gen, scns))
        print('gen done', STATS); return
    if a.step == 'rejudge':
        by = {s['id']: s for s in scns}
        def rj(f):
            r = json.loads(f.read_text(encoding='utf-8'))
            if r['scenario'] not in by: return
            g = judge(by[r['scenario']], r['first'], r['rest'])
            r.update(scores=g['scores'], notes=g.get('notes'), score=sum(g['scores']) / len(g['scores']))
            f.write_text(json.dumps(r, ensure_ascii=False, indent=2), encoding='utf-8'); print('RJ', r['id'], round(r['score'], 2), flush=True)
        with cf.ThreadPoolExecutor(a.workers) as ex: list(ex.map(rj, sorted((HERE / RES).glob('*.json'))))
        return
    jobs = [(m, c, s, r) for s in scns for c in (a.conds.split(',')) for m in MODELS for r in range(1, a.reps + 1)]
    random.Random(7).shuffle(jobs)
    with cf.ThreadPoolExecutor(a.workers) as ex: list(ex.map(lambda j: one(*j), jobs))
    print('run done', STATS)

if __name__ == '__main__':
    main()
