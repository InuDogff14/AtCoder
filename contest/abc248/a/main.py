def find_missing_digit(S):
    all_digits_sum = sum(range(10))  # 0から9の合計は45
    given_digits_sum = sum(map(int, S))  # Sの各数字を整数に変換して合計
    return all_digits_sum - given_digits_sum  # 足りない数字を求める

# 入力
S = input().strip()
print(find_missing_digit(S))