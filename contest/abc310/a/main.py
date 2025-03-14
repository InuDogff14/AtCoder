n,p,q = map(int,input().split())

d = list(map(int,input().split()))

ans = p

for price in d:
    if q + price < ans:
        ans = q + price
        
print(ans)