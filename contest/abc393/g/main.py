'''
1. 素数判定（エラトステネスの篩）
'''
def sieve(n):
    """n以下の素数を求める（エラトステネスの篩）"""
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]


'''
2. 組み合わせ計算（nCr）
'''
MOD = 998244353
def comb(n, r, mod=MOD):
    if r > n or r < 0:
        return 0
    fact = [1] * (n + 1)
    inv_fact = [1] * (n + 1)
    for i in range(2, n + 1):
        fact[i] = fact[i - 1] * i % mod
    inv_fact[n] = pow(fact[n], mod - 2, mod)
    for i in range(n - 1, 0, -1):
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % mod
    return fact[n] * inv_fact[r] % mod * inv_fact[n - r] % mod


'''
3. 動的計画法（DP）
(1) ナップサック DP（個数制限なし）
'''
def knapsack(values, weights, W):
    """個数制限なしナップサック DP"""
    dp = [0] * (W + 1)
    for w, v in zip(weights, values):
        for j in range(w, W + 1):
            dp[j] = max(dp[j], dp[j - w] + v)
    return dp[W]


'''
(2) ナップサック DP（個数制限あり）
'''
def knapsack_limited(values, weights, W):
    """個数制限ありナップサック DP"""
    N = len(values)
    dp = [[0] * (W + 1) for _ in range(N + 1)]
    for i in range(N):
        for j in range(W + 1):
            dp[i + 1][j] = dp[i][j]  # 使わない
            if j >= weights[i]:
                dp[i + 1][j] = max(dp[i + 1][j], dp[i][j - weights[i]] + values[i])
    return dp[N][W]


'''
4. Union-Find (Disjoint Set Union, DSU)
'''
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # 経路圧縮
        return self.parent[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return
        if self.rank[xr] > self.rank[yr]:
            self.parent[yr] = xr
        else:
            self.parent[xr] = yr
            if self.rank[xr] == self.rank[yr]:
                self.rank[yr] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)
    

'''
5. 累積和（Prefix Sum）
'''
def prefix_sum(arr):
    """配列の累積和を計算する"""
    n = len(arr)
    psum = [0] * (n + 1)
    for i in range(n):
        psum[i + 1] = psum[i] + arr[i]
    return psum
'''
# 例: 区間 [l, r) の和を求める
psum = prefix_sum([3, 1, 4, 1, 5])
l, r = 1, 4
print(psum[r] - psum[l])  # → 6 (1+4+1)
'''



'''
6. 二分探索（Binary Search）
'''
import bisect
arr = [1, 3, 5, 7, 9]

x = 4
idx = bisect.bisect_left(arr, x)  # x 以上の最小の要素の位置
print(idx)  # → 2 (5 の位置)

x = 5
idx = bisect.bisect_right(arr, x)  # x より大きい最小の要素の位置
print(idx)  # → 3 (7 の位置)


'''
7. べき乗（繰り返し二乗法）
'''
def mod_pow(a, b, mod=998244353):
    """a^b % mod を求める (O(log b))"""
    res = 1
    while b:
        if b & 1:
            res = res * a % mod
        a = a * a % mod
        b //= 2
    return res