from collections import Counter

n = int(input())
a = list(map(int, input().split()))

result = []
left_set = set()
right_counter = Counter(a)

for i in range(n - 1):
    left_set.add(a[i])
    right_counter[a[i]] -= 1
    if right_counter[a[i]] == 0:
        del right_counter[a[i]]  # 個数が0になったら削除
    result.append(len(left_set) + len(right_counter))

print(max(result))
