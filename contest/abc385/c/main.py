n = int(input())
s = list(map(str,input().split()))

# DPテーブル
dp = {}  # (高さ, 間隔) -> 最大長

max_len = 1  # 最小でも1つのビルは選べる

for i in range(n):
    for j in range(i):
        d = i - j  # 間隔
        if s[i] == s[j]:  # 同じ高さのビル
            if (s[j], d) in dp:
                dp[(s[i], d)] = dp[(s[j], d)] + 1
            else:
                dp[(s[i], d)] = 2  # j, i の2つのビルを選んだ
            max_len = max(max_len, dp[(s[i], d)])

print(max_len)