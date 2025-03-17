n,m = map(int,input().split())

a = []
b = []

for _ in range(m):
    ai,bi = map(int,input().split())
    a.append(ai)
    b.append(bi)
    
from collections import defaultdict

# グラフの構築
graph = defaultdict(list)
for u, v in zip(a, b):
    graph[v].append(u)

test = graph.keys()

def find_missing_number(test, N):
    expected_sum = N * (N + 1) // 2  # 1 から N までの合計
    actual_sum = sum(test)            # リスト内の合計
    return expected_sum - actual_sum

if len(test) == n-1:
    print(find_missing_number(test, n))
else:
    print(-1)
    
        