H,W = map(int,input().split())

s = [input()for _ in range(H)]

ax,ay,bx,by = 1000,1000,0,0

for i in range(0,H):
    for j in range(0,W):
        if s[i][j] == "#":
            ax = min(ax, i)
            bx = max(bx, i)
            ay = min(ay, j)
            by = max(by, j)

ans = "Yes"
for i in range(ax, bx + 1):
    for j in range(ay, by + 1):
        if s[i][j] == ".":
            ans = "No"

print(ans)