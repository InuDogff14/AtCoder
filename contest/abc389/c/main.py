import sys
from collections import deque

def solve(queries):
    snake_queue = deque()  # 各ヘビの長さを管理
    offset = 0  # 先頭のヘビの座標
    result = []
    
    for query in queries:
        q = query[0]

        if q == 1:
            # 1 l : ヘビを追加
            l = query[1]
            snake_queue.append(l)
        
        elif q == 2:
            # 2 : 先頭のヘビを削除
            m = snake_queue.popleft()
            offset += m  # 先頭座標を m だけずらす
        
        elif q == 3:
            # 3 k : k 番目のヘビの座標を求める
            k = query[1]
            pos = offset  # 先頭ヘビの座標
            for i in range(k - 1):  # k-1 匹分の累積和を加算
                pos += snake_queue[i]
            result.append(str(pos))
    
    print("\n".join(result))  # まとめて出力

# 標準入力から読み込む
if __name__ == "__main__":
    input = sys.stdin.read
    data = input().splitlines()
    
    Q = int(data[0])  # クエリ数
    queries = [list(map(int, line.split())) for line in data[1:Q+1]]
    
    solve(queries)
