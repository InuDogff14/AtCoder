a,b = map(int,input().split())

if b - a == 1:
    if a % 3 == 0:
        print('No')
        exit()
    else:
        print('Yes')
        exit()

print('No')
    