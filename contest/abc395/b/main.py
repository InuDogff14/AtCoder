N = int(input())
target = [["?"] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if min(i, j, N - i - 1, N - j - 1) % 2 == 0:
            target[i][j] = "#"
        else:
            target[i][j] = "."
for row in target:
    print("".join(row))