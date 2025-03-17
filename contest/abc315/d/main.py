h,w = map(int,input().split())

c = []
for _ in range(h):
    ci = list(input().strip())
    c.append(ci)
    
print(set(c))