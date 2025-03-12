import math

# エラトステネスの篩で素数リストを生成する
def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    primes = []
    
    for num in range(2, limit + 1):
        if sieve[num]:
            primes.append(num)
            for multiple in range(num * num, limit + 1, num):
                sieve[multiple] = False
                
    return primes

def solve(n):
    # N 以下の素数リストを生成
    limit = int(math.sqrt(n)) + 1
    primes = sieve_of_eratosthenes(limit)
    count = 0
    
    # a, b, c を選んで条件を満たすか確認
    for i in range(len(primes)):
        a = primes[i]
        a2 = a ** 2  # a^2 は繰り返し計算を避けるため事前に計算
        if a2 * primes[i] * primes[i] > n:  # この段階で条件に合わないならスキップ
            break
        for j in range(i + 1, len(primes)):
            b = primes[j]
            b2 = b ** 2  # b^2 も事前に計算
            if a2 * b * b2 > n:  # この段階で条件に合わないならスキップ
                break
            for k in range(j + 1, len(primes)):
                c = primes[k]
                if a2 * b * c ** 2 <= n:
                    count += 1
                else:
                    break
    
    print(count)

# 入力を受け付けて処理を呼び出す
n = int(input())
print(sieve_of_eratosthenes(int(math.sqrt(n))+1))
# solve(n)
