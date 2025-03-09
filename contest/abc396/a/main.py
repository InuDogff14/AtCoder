def Triple_Four(N,A):
    for i in range(N -2):
        if A[i] == A[i+1] == A[i+2]:
            return 'Yes'
    return 'No'

N = int(input())  # Nの値
A = list(map(int, input().split()))  # Aのリスト

print(Triple_Four(N,A))

