from collections import defaultdict

# 入力を読み込む
N, M = map(int, input().split())

# 辺のカウント用の辞書
edge_count = defaultdict(int)

# 取り除くべき辺の数
remove_count = 0

# 辺の情報を処理
for _ in range(M):
    u, v = map(int, input().split())
    
    # 自己ループの場合
    if u == v:
        remove_count += 1
    else:
        # u と v の順番を統一するため、u < v の場合に処理
        if u > v:
            u, v = v, u
        
        # 辺(u, v)のカウントを増やす
        edge_count[(u, v)] += 1

# 多重辺を取り除くための処理
for count in edge_count.values():
    if count > 1:
        remove_count += count - 1  # 多重辺は余分な分を取り除く

# 結果を出力
print(remove_count)
