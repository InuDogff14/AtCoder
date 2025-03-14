N, M = map(int, input().split())

P = []  # P[i]: 商品iの値段
F = []  # F[i]: 商品iの機能のセット
for _ in range(N):
    p, c, *f = map(int, input().split())
    P.append(p)
    se = set()
    for el in f:
        se.add(el)
    F.append(se)

for i in range(N):
    for j in range(N):
        if i == j:
            continue  # 自分自身はスキップ
        
        if P[i] >= P[j] and F[i].issubset(F[j]):
            if P[i] > P[j] or len(F[j] - F[i]) > 0:
                print('Yes')
                exit()

print('No')