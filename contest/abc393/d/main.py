# 入力を受け取る
N = int(input())
S = input()

# '1'の位置を全てリストに記録
ones_positions = [i for i, char in enumerate(S) if char == '1']

# 1の数
one_count = len(ones_positions)

# 中央の位置を選ぶ（中央値を基準にすると最小の移動回数で済む）
median_index = one_count // 2

# 目標となる位置は、中央値を中心に並べる
target_positions = [ones_positions[median_index] - (median_index - i) for i in range(one_count)]

# 移動回数を求める（各1を目標位置に移動する回数）
min_operations = sum(abs(ones_positions[i] - target_positions[i]) for i in range(one_count))

# 結果を出力
print(min_operations)