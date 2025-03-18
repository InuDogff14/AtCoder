n = int(input())

a,b,c,d = [],[],[],[]

for _ in range(n):
    ai,bi,ci,di = map(int,input().split())
    a.append(ai)
    b.append(bi)
    c.append(ci)
    d.append(di)
max_x = max(b)
max_y = max(d)
lst = [[0] * max_x for _ in range(max_y)]

for i in range(n):
    x1,x2,y1,y2 = a[i],b[i],c[i],d[i]
    for j in range(y1,y2):
        for k in range(x1,x2):
            lst[j][k] += 1

count = sum(cell >= 1 for row in lst for cell in row)
print(count)

    