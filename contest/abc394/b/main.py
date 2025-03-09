import sys

# 標準入力からすべての行を取得
lines = sys.stdin.read().splitlines()

# 1行目をNとして取得
N = int(lines[0])

# 2行目以降をリスト S に格納
S = lines[1:N+1]

S.sort(key=len)

print("".join(S))