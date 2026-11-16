import json, statistics as st
from pathlib import Path
from collections import defaultdict
import sys
R = Path(__file__).resolve().parent / (sys.argv[1] if len(sys.argv) > 1 else 'results')
rows = [json.loads(f.read_text(encoding='utf-8')) for f in R.glob('*.json')]
rows = [r for r in rows if 'score' in r]
def agg(key):
    d = defaultdict(list)
    for r in rows: d[key(r)].append(r)
    return d
print('样本数', len(rows))
for title, key in [('按组', lambda r: r['cond']), ('组×场景类型', lambda r: (r['cond'], r['kind'])),
                   ('组×模型', lambda r: (r['cond'], r['model'])), ('组×场景', lambda r: (r['scenario'], r['cond']))]:
    print('\n==', title)
    for k, v in sorted(agg(key).items(), key=lambda x: str(x[0])):
        full = sum(1 for r in v if r['score'] == 1)
        print(k, f"均分 {st.mean(r['score'] for r in v):.2f}", f"全对 {full}/{len(v)}",
              f"交接长度中位 {int(st.median(r['handover_chars'] for r in v))}字")
# 丢分最多的题
miss = defaultdict(lambda: defaultdict(int))
for r in rows:
    for i, s in enumerate(r['scores']):
        if s == 0: miss[(r['scenario'], i + 1)][r['cond']] += 1
print('\n== 丢分题（场景,题号）: 各组丢分次数')
for k, v in sorted(miss.items(), key=lambda x: -sum(x[1].values())):
    print(k, dict(v))
