INF = 10 ** 20

n = int(input())

a, b = [], []
for _ in range(n):
    x, y = map(int, input().split())
    a.append(x)
    b.append(y)

prob = dict()

i = 1

for n,m in zip(a,b):
    proba = INF * n // (n + m)
    prob[i] = proba
    i +=1
    
sorted_data = dict(sorted(prob.items(), key=lambda x: x[1],reverse=True))
print(*sorted_data.keys())