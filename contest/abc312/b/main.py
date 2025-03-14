n,m = map(int,input().split())

s = []

for _ in range(n):
    item = input()
    s.append(item)
ans = []

def is_tak(si, sj):
    for i in range(si, si + 3):
        for j in range(sj, sj + 3):
            if s[i][j] != '#':
                return False
    for i in range(si + 6, si + 9):
        for j in range(sj + 6, sj + 9):
            if s[i][j] != '#':
                return False
    for i in range(si, si + 4):
        if s[i][sj + 3] != '.':
            return False
    for i in range(si + 5, si + 9):
        if s[i][sj + 5] != '.':
            return False
    for j in range(sj, sj + 4):
        if s[si + 3][j] != '.':
            return False
    for j in range(sj + 5, sj + 9):
        if s[si + 5][j] != '.':
            return False
    return True
for i in range(n-8):
    for j in range(m-8):
        if is_tak(i,j):
            print(i+1,j+1)
            