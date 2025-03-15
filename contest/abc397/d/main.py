def find_x_y(N):
    y = 1
    # x^3 - y^3 = N を満たす (x, y) を探す
    while True:
        y_cubed = y ** 3
        # x^3 = N + y^3 の形
        x_cubed = N + y_cubed
        
        # x_cubed が立方数かどうかを確認
        x = int(round(x_cubed ** (1 / 3)))
        
        # 立方根を計算して整数ならばx^3 == N + y^3かを確認
        if x ** 3 == x_cubed:
            return x, y
        
        # yを増やす
        y += 1
        
        # 上限の設定
        if y > 10**6:  # y の最大値を10^6に設定
            break
    
    return -1

# 入力を受け取る
N = int(input())

# 結果を表示
result = find_x_y(N)
if result == -1:
    print(-1)
else:
    print(result[0], result[1])
