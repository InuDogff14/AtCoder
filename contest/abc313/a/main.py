n = int(input())
p = list(map(int,input().split()))

max_val = 0

if len(p) > 1:
    max_val = max(p[1:])
if len(p) == 1:
    print(0)
    exit()

result = 0

if p[0] <= max_val:
    result = max_val - p[0] +1

print(result)