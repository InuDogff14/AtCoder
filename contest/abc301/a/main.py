n = int(input())
s = input()

if s.count('T') > s.count('A'):
    print('T')
    exit()
elif s.count('T') == s.count('A'):
    if s[n-1] == 'T':
        print('A')
        exit()
    print('T')
    exit()
print('A')