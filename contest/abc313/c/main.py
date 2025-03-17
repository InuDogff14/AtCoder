n = int(input())
a = list(map(int,input().split()))

if len(a) == 1:
    print(0)
    exit()
    
mean_value = sum(a) / len(a)

above_avg = [x for x in a if x >= mean_value]
below_avg = [x for x in a if x < mean_value]

sum_a = sum(above_avg)
sum_b = sum(below_avg)

ans = (sum_a - sum_b) // max(len(above_avg),len(below_avg))
print(ans)