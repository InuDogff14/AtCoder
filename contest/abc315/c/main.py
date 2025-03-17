from itertools import combinations
from collections import defaultdict

n = int(input())

f = []
s = []

for _ in range(n):
    fi,si = map(int,input().split())
    f.append(fi)
    s.append(si)

z = zip(f,s)
result = []
for key1,key2 in combinations(z,2):
    if key1[0] == key2[0]:
        if key1[1] >= key2[1]:
            r =key1[1] + (key2[1] // 2)
            result.append(r)
        else:
            r =key2[1] + (key1[1] // 2)
            result.append(r)
    else:
        r = key1[1] + key2[1]
        result.append(r)
        
print(max(result))