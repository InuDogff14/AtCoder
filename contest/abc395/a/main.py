N = int(input())
A = list(map(int, input().split()))

val = 'Yes'

for i in range(0,N-1):
    if A[i] >= A[i+1]:
        val = 'No'
        break

print(val)