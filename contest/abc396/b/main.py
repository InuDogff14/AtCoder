import sys

# 入力を一度に受け取る
input = sys.stdin.read
data = input().splitlines()

# クエリの数 Q を取得
Q = int(data[0])

# 山を表すリスト（初期状態ではカード 0 が 100 枚積まれている）
stack = [0] * 100  # 最初に 0 のカードが 100 枚積まれている

# 出力を一度にまとめるためのリスト
output = []

# クエリ処理
for i in range(1, Q + 1):
    query = data[i].replace('_', ' ').split()  # '_ 'をスペースに変換してから分割
    query = list(map(int, query))  # クエリを整数に変換
    if query[0] == 1:
        # タイプ 1 のクエリ: x のカードを積む
        x = query[1]
        stack.append(x)  # 一番上に x を積む
    elif query[0] == 2:
        # タイプ 2 のクエリ: 一番上のカードを取り除き、その値を出力
        top_card = stack.pop()  # 一番上のカードを取り除く
        output.append(str(top_card))  # 取り除いたカードの整数を出力用リストに追加

# 結果を一度に出力
sys.stdout.write("\n".join(output) + "\n")
