import sys

def solve(N, Q, queries):
    # 鳩の現在の巣を管理するリスト
    pigeon_location = list(range(N))  # 鳩 i は巣 i にいる (0-indexed)
    # 巣ごとの鳩の数を管理するリスト
    nest_count = [1] * N  # 初めは各巣に1羽ずつ
    # 複数の鳩がいる巣の数
    multi_nest_count = 0
    
    result = []
    
    for query in queries:
        if query[0] == 1:
            P, H = query[1] - 1, query[2] - 1  # 0-indexed に変換
            old_nest = pigeon_location[P]
            new_nest = H
            
            # 古い巣から鳩を移動
            nest_count[old_nest] -= 1
            if nest_count[old_nest] == 1:
                multi_nest_count -= 1  # 2羽以上いた巣が1羽になった場合減らす
            
            # 新しい巣に鳩を移動
            if nest_count[new_nest] == 1:
                multi_nest_count += 1  # 1羽から2羽になった場合増やす
            nest_count[new_nest] += 1
            
            pigeon_location[P] = new_nest
            
        elif query[0] == 2:
            result.append(str(multi_nest_count))
    
    print("\n".join(result))

if __name__ == "__main__":
    input = sys.stdin.read
    data = input().splitlines()
    
    N, Q = map(int, data[0].split())
    queries = [list(map(int, line.split())) for line in data[1:Q+1]]
    
    solve(N, Q, queries)