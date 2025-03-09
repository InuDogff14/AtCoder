def find_shortest_subarray_with_duplicates(N, A):
    # 値の最初の出現位置を記録する辞書
    position_map = {}
    min_length = float('inf')  # 最小の長さを保持する変数

    for i in range(N):
        if A[i] in position_map:
            # すでに出現した場合、その距離を計算
            length = i - position_map[A[i]] + 1
            min_length = min(min_length, length)
        # 現在の値の位置を記録
        position_map[A[i]] = i
    
    # 結果として最小の長さを返す
    return min_length if min_length != float('inf') else -1

# 入力の読み込み
N = int(input())
A = list(map(int, input().split()))

# 結果を出力
print(find_shortest_subarray_with_duplicates(N, A))
