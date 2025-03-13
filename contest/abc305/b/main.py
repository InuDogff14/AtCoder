p,q = map(str,input().split())

temp = {'A':3,'B':1,"C":4,"D":1,"E":5,"F":9,"G":0}

if p < q:
    start = p
    end =q
else:
    start = q
    end = p

d = 0
sum_value = 0

found = False

for key in temp:
    if key == start:
        found = True
    if key == end:
        break
    if found:
        sum_value += temp[key]
    

print(sum_value)