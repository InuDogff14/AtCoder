n,k = map(int,input().split())

a,b = [],[]

for _ in range(n):
    x,y = map(int,input().split())
    a.append(x)
    b.append(y)

total = sum(b)

sort_zip = sorted(zip(a,b), key = lambda x:x[0])

if total <= k:
    print(1)
    exit()

for n, m in sort_zip:
        total -= m
        if total <= k:
            print(n+1)
            exit()
        