m = int(input())

d = list(map(int,input().split()))

sum = sum(d)

if sum % 2 == 1:
    sum += 1

mid = sum // 2

total = 0
count = 1
prev = 0
for v in d:
    total += v
    if total >= mid:
        ans = v - (total - mid)
        print(count, ans)
        exit()
    count += 1
    prev = v