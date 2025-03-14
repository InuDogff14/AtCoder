from itertools import combinations

n = int(input())

s= []

for _ in range(n):
    item = input().strip()
    s.append(item)

seen = {}
ans = n

for i in range(n):
    if s[i] in seen or s[i][::-1] in seen:
        ans -= 1
    seen[s[i]] = True
print(ans)
        