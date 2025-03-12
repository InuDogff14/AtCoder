from itertools import permutations

def is_one_char_diff(str1, str2):
    # 2つの文字列が1文字だけ異なるか判定
    diff_count = sum(c1 != c2 for c1, c2 in zip(str1, str2))
    return diff_count == 1

def solve(n, m, strings):
    # 全順列を試す
    for perm in permutations(strings):
        if all(is_one_char_diff(perm[i], perm[i + 1]) for i in range(n - 1)):
            print("Yes")
            return
    print("No")

# 入力処理
def main():
    n, m = map(int, input().split())
    strings = [input().strip() for _ in range(n)]
    solve(n, m, strings)

if __name__ == "__main__":
    main()
