MOD = 998244353

def count_valid_sequences(N, M, K):
    dp = [[0] * (K + 1) for _ in range(N + 1)]
    dp[0][0] = 1  # 初期状態

    for i in range(N):  # i 番目の要素を決める
        for j in range(K + 1):  # 今の合計
            if dp[i][j] == 0:
                continue
            for a in range(1, M + 1):  # 1 から M までの数字を選ぶ
                if j + a <= K:
                    dp[i + 1][j + a] = (dp[i + 1][j + a] + dp[i][j]) % MOD

    return sum(dp[N]) % MOD  # N 個選んだときの合計が K 以下のものすべてを足す

# 入力
N, M, K = map(int, input().split())
print(count_valid_sequences(N, M, K))
