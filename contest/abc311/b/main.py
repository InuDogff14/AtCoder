n,d = map(int,input().split())

s = []
for _ in range(n):
    item = input()
    s.append(item)



ans = 0
val = 0
streak = False

for i in range(d):
    count = 0
    for j in range(n):
        if s[j][i] == 'o':
            count += 1
        
    if count == n:
        val += 1
        streak = True
    else:
        if streak:
            ans = max(ans,val)
            val =0
            streak = False

ans = max(val,ans)
print(ans)