from collections import deque

n = int(input())
s = input()

q = deque(s)
result =''

while q:
    char = q.popleft()
    result += char*2

print(result)
