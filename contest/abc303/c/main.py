N, M, H, K = map(int, input().split())
S = input()
heal = set()
for _ in range(M):
    x, y = map(int, input().split())
    heal.add((x, y))

st = 'RLUD'
tmp = [(1, 0), (-1, 0), (0, 1), (0, -1)]
dic = dict()
for s, t in zip(st, tmp):
    dic[s] = t

nx, ny = 0, 0
for s in S:
    vx, vy = dic[s]
    nx += vx
    ny += vy
    H -= 1

    if H < 0:
        print('No')
        exit()

    if H < K and (nx, ny) in heal:
        H = K
        heal.discard((nx, ny))

print('Yes')

