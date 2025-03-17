from collections import defaultdict

n,m = map(int,input().split())
s = input().strip()
c = list(map(int,input().split()))

z = zip(c,s)

grouped = defaultdict(list)
for k, v in z:
    grouped[k].append(v)

for k in grouped:
    grouped[k] = [grouped[k][-1]] + grouped[k][:-1]
    
# 元の形式に戻して文字列に変換
shifted_data = []
index = {k: 0 for k in grouped}  # 各キーのインデックス管理
for k, _ in z:
    shifted_data.append(f"({k}, '{grouped[k][index[k]]}')")
    index[k] += 1

print(shifted_data)