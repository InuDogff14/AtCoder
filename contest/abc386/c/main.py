def levenshtein_distance(a: str, b: str) -> int:
    la, lb = len(a), len(b)
    
    # DPテーブルを作成 (la+1) x (lb+1)
    dp = [[0] * (lb + 1) for _ in range(la + 1)]
    
    # 初期化 (空文字列にするための操作回数)
    for i in range(la + 1):
        dp[i][0] = i  # a の i 文字目までを削除
    for j in range(lb + 1):
        dp[0][j] = j  # b の j 文字目までを挿入

    # DP 更新
    for i in range(1, la + 1):
        for j in range(1, lb + 1):
            cost = 0 if a[i-1] == b[j-1] else 1  # 文字が同じならコスト0、違えば1
            dp[i][j] = min(
                dp[i-1][j] + 1,     # 削除 (a[i-1] を消す)
                dp[i][j-1] + 1,     # 挿入 (b[j-1] を追加)
                dp[i-1][j-1] + cost # 置換 (a[i-1] → b[j-1])
            )

    return dp[la][lb]

k = int(input())
s = input()
t = input()
if levenshtein_distance(s,t) <= 1:
    print('Yes')
else:
    print('No')

