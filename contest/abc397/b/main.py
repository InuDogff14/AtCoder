def solve(S):
    # 挿入回数のカウンタ
    count = 0
    if S[0] == 'o':
        count += 1
    # 文字列の各文字を順に見ていく
    for i in range(len(S)):
        if (i + count) % 2 == 0:  # 0, 2, 4, ... 番目は 'i' が必要
            if S[i] != 'i':
                count += 1
        else:  # 1, 3, 5, ... 番目は 'o' が必要
            if S[i] != 'o':
                count += 1
    # 長さが奇数なら、最初に挿入する必要がある
    if S[len(S) -1] == 'i':
        count += 1
    return count

# 入力を受け取る
S = input().strip()

# 結果を出力
print(solve(S))
