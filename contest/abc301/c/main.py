cards = ['a','t','c','o','d','e','r']

def solve(s):
    return any(char in s  for char in cards)

s = set(input())
t = set(input())

if solve(s-t) and solve(t-s):
    print('Yes')
    exit()
print('No')