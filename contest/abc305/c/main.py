H, W = map(int, input().split())
grid = [input().strip() for _ in range(H)]

# クッキーがある最小/最大の行と列を特定
min_i, max_i = H, 0
min_j, max_j = W, 0

for i in range(H):
    for j in range(W):
        if grid[i][j] == '#':
            min_i = min(min_i, i)
            max_i = max(max_i, i)
            min_j = min(min_j, j)
            max_j = max(max_j, j)

# クッキーが食べられたマスを探す
for i in range(min_i, max_i + 1):
    for j in range(min_j, max_j + 1):
        if grid[i][j] == '.':
            print(i + 1, j + 1)
            exit()
