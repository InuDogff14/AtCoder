def count_batsu(grid, H, W):
    N = min(H, W)
    counts = [0] * (N + 1)
    
    # 各マスを探索
    for a in range(H):
        for b in range(W):
            if grid[a][b] == '#':
                # 各方向の最大距離を確認
                max_n = N
                for n in range(1, N + 1):
                    if not all([
                        a + n < H and b + n < W and grid[a + n][b + n] == '#',
                        a + n < H and b - n >= 0 and grid[a + n][b - n] == '#',
                        a - n >= 0 and b + n < W and grid[a - n][b + n] == '#',
                        a - n >= 0 and b - n >= 0 and grid[a - n][b - n] == '#'
                    ]):
                        max_n = n - 1
                        break
                
                if max_n >= 1:
                    counts[max_n] += 1

    print(*counts[1:])

# 入力例
h,w = map(int,input().split())

c = []

for _ in range(h):
    item = list(input().strip())
    c.append(item)
count_batsu(c,h,w)
    
