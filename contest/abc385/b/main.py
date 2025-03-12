h, w, x, y = map(int, input().split())

s = []
for _ in range(h):
    val = list(input().strip())  # 1文字ずつ取得
    s.append(val)

t = list(input().strip())  # 移動指示を1文字ずつ取得
count = 0

x = x-1
y= y-1

# 初期位置が '@' ならカウントする
if s[x][y] == '@':
    count += 1
    s[x][y] = '.'

for item in t:
    if item == "U" and x > 0 and s[x-1][y] != '#':
        x -= 1
    elif item == "D" and x < h-1 and s[x+1][y] != '#':
        x += 1
    elif item == "L" and y > 0 and s[x][y-1] != '#':
        y -= 1
    elif item == "R" and y < w-1 and s[x][y+1] != '#':
        y += 1
    
    if s[x][y] == '@':
        count += 1
        s[x][y] = '.'

print(x+1, y+1, count)
