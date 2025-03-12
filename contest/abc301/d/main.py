s = input()
n = int(input())

from itertools import product

def fill_placeholders(s):
    count = s.count('?')
    combinations = product('01', repeat=count)
    
    result = []
    for combo in combinations:
        filled = s
        for c in combo:
            filled = filled.replace('?', c, 1)
        result.append(filled)
    
    return result

binarys = fill_placeholders(s)

max_val = -1

for binary in binarys:
    if n > int(binary,2):
        max_val = int(binary,2)

print(max_val)


