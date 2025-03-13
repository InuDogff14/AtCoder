s = list(map(int,input().split()))

prev_num = 0
for num in s:
    if num % 5 != 0:
        print('No')
        exit()
    if num < 100 or num > 675:
        print('No')
        exit()
    if num < prev_num:
        print('No')
        exit()
    prev_num = num

print('Yes')
    