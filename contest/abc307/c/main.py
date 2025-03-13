def can_match(Ha, Wa, A, Hb, Wb, B, Hx, Wx, X):
    # シートAとBの黒マスの位置を取得
    A_black = [(i, j) for i in range(Ha) for j in range(Wa) if A[i][j] == '#']
    B_black = [(i, j) for i in range(Hb) for j in range(Wb) if B[i][j] == '#']
    X_black = [(i, j) for i in range(Hx) for j in range(Wx) if X[i][j] == '#']

    # シートAを(xa, ya)に、シートBを(xb, yb)に配置
    for xa in range(-Ha + 1, Hx):
        for ya in range(-Wa + 1, Wx):
            for xb in range(-Hb + 1, Hx):
                for yb in range(-Wb + 1, Wx):
                    # 結果用のグリッド
                    grid = [['.'] * Wx for _ in range(Hx)]

                    # シートAの黒マスを配置
                    for ai, aj in A_black:
                        ni, nj = ai + xa, aj + ya
                        if 0 <= ni < Hx and 0 <= nj < Wx:
                            grid[ni][nj] = '#'

                    # シートBの黒マスを配置
                    for bi, bj in B_black:
                        ni, nj = bi + xb, bj + yb
                        if 0 <= ni < Hx and 0 <= nj < Wx:
                            grid[ni][nj] = '#'

                    # 配置した結果がXと一致するか確認
                    if all(grid[i][j] == X[i][j] for i in range(Hx) for j in range(Wx)):
                        return "Yes"
    
    return "No"

# 入力処理
Ha, Wa = map(int, input().split())
A = [input().strip() for _ in range(Ha)]
Hb, Wb = map(int, input().split())
B = [input().strip() for _ in range(Hb)]
Hx, Wx = map(int, input().split())
X = [input().strip() for _ in range(Hx)]

# 判定
print(can_match(Ha, Wa, A, Hb, Wb, B, Hx, Wx, X))
