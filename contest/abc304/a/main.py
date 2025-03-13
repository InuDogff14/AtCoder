n = int(input())

s = []
a = []

for _ in range(n):
    x,y = map(str,input().split())
    s.append(x)
    a.append(int(y))

min_age = min(a)
index = a.index(min_age)

ans = []
val = n - index

for i in range(index,n):
    ans.append(s[i])
    
if n - len(ans) != 0:
    for j in range(n-len(ans)):
        ans.append(s[j])

for f in ans:
    print(f)