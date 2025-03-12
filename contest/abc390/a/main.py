A = list(map(int,input().split()))

count = 0

for i in range(len(A)-1):
    if A[i] > A[i+1]:
        count += 1

if count == 1:
    print('Yes')
else:
    print('No')