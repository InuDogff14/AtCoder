n = int(input())
a = list(map(int, input().split()))

diff = [0] * (n + 10)
for i, a_i in enumerate(a):
    present = min(a_i, n - i - 1)
    a[i] -= present
    diff[i + 1] += 1
    diff[min(n, i + 1 + present)] -= 1
    diff[i + 1] += diff[i]
    if i + 1 < n:
        a[i + 1] += diff[i + 1]

print(*a)