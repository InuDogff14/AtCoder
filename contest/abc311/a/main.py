n = int(input())
s = input()

isa= False
isb = False
isc = False

for i in range(n):
    if s[i] == 'A':
        isa = True
    elif s[i] == 'B':
        isb = True
    else:
        isc = True
    
    if isa and isb and isc:
        print(i+1)
        exit()