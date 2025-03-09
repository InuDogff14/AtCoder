N,M = map(int,input().split())
A = list(map(int,input().split()))

numbers = list(range(1, N + 1))
    
if N == M:
    print(0)
    print()
else:
    for n in A:
        if n in numbers:
            numbers.remove(n)
    print(len(numbers))
    print(*numbers)
            
