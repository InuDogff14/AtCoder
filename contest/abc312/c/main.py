from bisect import bisect_right, bisect_left

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()


def judge(m):
    c1 = bisect_right(A, m)
    c2 = M - bisect_left(B, m)
    return c1 >= c2


ok, ng = 10 ** 9 + 1, 0
while ok - ng > 1:
    mid = (ok + ng) // 2
    if judge(mid):
        ok = mid
    else:
        ng = mid
print(ok)

