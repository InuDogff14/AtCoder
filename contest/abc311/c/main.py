m = int(input())
a = [int(t) - 1 for t in input().split()]

seen = [0]
se  = {0}
v = 0

while True:
    nv = a[v]
    if nv in se:
        idx = seen.index(nv)
        ans_list = seen[idx:]
        print(len(ans_list))
        print(*ans_list)
        break
    else:
        se.add(nv)
        seen.append(nv)
        v = nv