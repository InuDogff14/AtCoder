def solve(S):
    # 文字列をリストとして扱って操作しやすくする
    S = list(S)
    
    # 操作を繰り返す
    i = 0
    while i < len(S) - 1:
        # 「WA」が連続して現れる場所を探す
        if S[i] == 'W' and S[i + 1] == 'A':
            # 見つかった「WA」を「AC」に置き換える
            S[i] = 'A'
            S[i + 1] = 'C'
            # 置き換えたのでiは次の文字に進む
            i = max(0, i - 1)  # 置き換えた前の文字で再チェックする
        else:
            # 「WA」が見つからない場合は次の文字へ
            i += 1
    
    # 結果のリストを文字列に戻して出力
    return ''.join(S)

# 入力を受け取る
S = input().strip()

# 解答を出力
print(solve(S))
