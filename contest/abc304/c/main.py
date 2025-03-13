from math import sqrt
from collections import deque

# 入力の受け取り
N, D = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(N)]

# D^2 を計算しておく（効率化のため）
D_squared = D * D

# 感染状態のリスト
infected = [False] * N

# 人1（インデックス0）が最初に感染している
infected[0] = True

# 感染者の管理用キュー（BFSを使用）
queue = deque([0])

# BFSの実行
while queue:
    current = queue.popleft()
    current_x, current_y = points[current]

    # 現在の感染者の周囲を調べる
    for i in range(N):
        if not infected[i]:
            x, y = points[i]
            # 距離の二乗を計算
            distance_squared = (current_x - x) ** 2 + (current_y - y) ** 2
            if distance_squared <= D_squared:
                # 感染者が近いので感染
                infected[i] = True
                queue.append(i)

# 結果の出力
for i in range(N):
    if infected[i]:
        print("Yes")
    else:
        print("No")
