N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(M)]

seen_pair = set()
for row in A:
    for i in range(N - 1):
        x, y = row[i], row[i + 1]
        seen_pair.add((x, y))
        seen_pair.add((y, x))

ans = N * (N - 1) // 2 - len(seen_pair) // 2
print(ans)
