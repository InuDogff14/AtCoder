h,w = map(int,input().split())
s=[]

for _ in range(h):
    item = input()
    s.append(item)

result = [[0,0]] * 5
for i in range(h):
    if s[i].find('s') != -1:
        result[0] = [i+1,s[i].find('s')+1]
    elif s[i].find('n') != -1:
        result[1] = [i+1,s[i].find('n')+1]
    elif s[i].find('u') != -1:
        result[2] = [i+1,s[i].find('u')+1]
    elif s[i].find('k') != -1:
        result[3] = [i+1,s[i].find('k')+1]
    elif s[i].find('e') != -1:
        result[4] = [i+1,s[i].find('e')+1]

print(*result)