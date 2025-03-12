H, W = map(int, input().split())

# グリッドを1次元リストに変換
A = [input().strip() for _ in range(H)]
B = [input().strip() for _ in range(H)]

# 各 (s, t) のシフトを試す
def shift_and_check(s, t):
    # 縦シフト
    shifted_A = A[-s:] + A[:-s]

    # 横シフト
    shifted_A = [''.join(row[-t:] + row[:-t]) for row in shifted_A]

    # 一致チェック
    return shifted_A == B

# すべての (s, t) の組み合わせを確認
for s in range(H):
    for t in range(W):
        if shift_and_check(s, t):
            print("Yes")
            exit()

print("No")