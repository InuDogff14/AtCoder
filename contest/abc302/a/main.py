a,b = map(int,input().split())

import math

if a % b ==0:
    print(a//b)
    exit()
print((a//b) + 1)