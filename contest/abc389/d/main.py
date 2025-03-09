import math

def solve(R):
    count = 0
    # 探索範囲を決定
    for i in range(-R, R+1):
        for j in range(-R, R+1):
            # 4つの頂点が円の中に収まるかチェック
            if (math.sqrt((i + 0.5)**2 + (j + 0.5)**2) <= R and
                math.sqrt((i + 0.5)**2 + (j - 0.5)**2) <= R and
                math.sqrt((i - 0.5)**2 + (j + 0.5)**2) <= R and
                math.sqrt((i - 0.5)**2 + (j - 0.5)**2) <= R):
                count += 1
    return count

# 入力を受け取る
R = int(input())
print(solve(R))


