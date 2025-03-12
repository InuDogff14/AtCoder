def expand_sequence(n, a):
    result = [a[0]]  # 初期値を追加
    for i in range(1, n):
        if abs(a[i] - a[i-1]) != 1:
            # 範囲を埋める要素を追加
            if a[i] > a[i-1]:
                result.extend(range(a[i-1] + 1, a[i]))
            else:
                result.extend(range(a[i-1] - 1, a[i], -1))
        result.append(a[i])
    
    # 出力
    print(" ".join(map(str, result)))

# 入力例
n = int(input())
a = list(map(int, input().split()))

expand_sequence(n, a)