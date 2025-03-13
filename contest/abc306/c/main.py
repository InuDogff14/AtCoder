n = int(input())

a = list(map(int,input().split()))

hashset = set(a)

if len(hashset) == 1:
    print(1)
    exit()

result = dict()
for num in hashset:
    first_index = a.index(num)
    second_index = a.index(num,first_index+1)
    result[num] = second_index+1

sort = dict(sorted(result.items(),key=lambda x : x[1]))

print(*sort.keys())