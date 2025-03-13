from itertools import combinations

n = int(input())
s = []

for _ in range(n):
    item = input()
    s.append(item)

def solve(s):
    return s == s[::-1]

for x,y in combinations(s,2):
    t = x + y
    if solve(t):
        print('Yes')
        exit()
        
    v = y + x
    if solve(v):
        print('Yes')
        exit()

print('No')
        