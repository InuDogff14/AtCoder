n,m,p = map(int,input().split())

result = []
ans = m

result.append(ans)
while ans <= n:
    ans += p
    result.append(ans)

c = len(result)

print(c-1)