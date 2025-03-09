S = input()

count = 0
n = len(S)

# 1番目の文字(A)の位置を i として、2番目の文字(B)の位置を j、3番目の文字(C)の位置を k とする
for i in range(n - 2):  # i の位置を探索
    if S[i] == 'A':
        for j in range(i + 1, n - 1):  # j の位置を探索 (i < j)
            if S[j] == 'B':
                # j - i が決まったので、k を求める
                k = 2 * j - i
                if k < n and S[k] == 'C':  # k の位置が文字列内で、かつ S[k] が 'C' であることを確認
                    count += 1

print(count)