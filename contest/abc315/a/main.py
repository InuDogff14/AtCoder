s = input()

l = ['a', 'e', 'i', 'o', 'u']

ans = ''

for char in l:
    s = s.replace(char,'')
    
print(s)