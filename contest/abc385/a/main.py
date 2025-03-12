from collections import deque
import sys

a = deque(list(map(int,input().split())))

max_val = max(a)
if len(set(a)) == 1:
    print('Yes')
    sys.exit()

a.remove(max_val)

if sum(a) == max_val:
    print('Yes')
else:
    print('No')