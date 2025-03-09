import math

def min_shouts_to_reach_B(A, B, K):
    if A >= B:
        return 0
    return math.ceil(math.log(B / A, K))

# 入力
A, B, K = map(int, input().split())
print(min_shouts_to_reach_B(A, B, K))