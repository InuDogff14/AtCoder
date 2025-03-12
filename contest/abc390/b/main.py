N = int(input())
A = list(map(int,input().split()))

a1 = A[0]
r = A[1] / A[0]

A_sum = sum(A)
S_n =0

if r == 1:
    S_n = N * a1
else:
    S_n = (a1*(r**N - 1)) / (r-1)
    
if A_sum == S_n:
    print('Yes')
else:
    print('No')