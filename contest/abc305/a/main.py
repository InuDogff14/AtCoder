n = int(input())

if n ==0 or n%5 == 0:
    print(n)
    exit()

mod = n % 5

if mod < 2.5:
    print(n-mod)

else:
    print(n+(5-mod))