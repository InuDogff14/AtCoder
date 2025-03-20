from collections import deque

n,m = map(int,input().split())
a = list(map(int,input().split()))
q = deque(a)

max_a = max(a)

lst = [i+1 for i in range(max_a)]

for v in lst:
    if v == q[0]:
        q.popleft()
        print(0)
    else:
        print(q[0]-v)

    