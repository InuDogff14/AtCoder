n = int(input())
a = []

for _ in range(n):
    item = input().strip()
    a.append(list(item))
b = [['0'] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == 0:
            if j == 0:
                b[i][j] = a[i+1][j]
            else:
                b[i][j] = a[i][j-1]
        elif i == n - 1:
            if j == n - 1:
                b[i][j] = a[i-1][j]
            else:
                b[i][j] = a[i][j+1]
        else:
            if j == 0:
                b[i][j] = a[i+1][j]
            elif j == n-1:
                b[i][j] = a[i-1][j]
            else:
                b[i][j] = a[i][j]
                
# 出力
for row in b:
    print("".join(row))  # 各行を文字列に戻して表示
            