n = int(input())
c = []
a= []

for _ in range(n):
    ci = int(input())
    ai = list(map(int,input().split()))
    c.append(ci)
    a.append(ai)

x = int(input())

z = zip(c,a)

result = {}

for i,(l,m) in enumerate(z):
    if x in m:
        result[i+1] = l

if len(result) == 0:
    print(0)
    exit()
min_value = min(result.values())
min_keys = [key for key, value in result.items() if value == min_value]
print(len(min_keys))
print(*min_keys)