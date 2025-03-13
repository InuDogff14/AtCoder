n = int(input())
a = list(map(int,input().split()))

b = []
count = 0
sum = 0
j = 0

for i in range(n*7):
    sum += a[i]
    count += 1
    if count == 7:
        b.append(sum)
        sum= 0 
        count =0
        j +=1


print(*b)