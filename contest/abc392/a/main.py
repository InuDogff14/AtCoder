a1 , a2 , a3 = map(int,input().split())

# 最大値を選ぶ
max_value = max(a1, a2, a3)

# 最大値以外の値をリストにする
other_values = [x for x in [a1, a2, a3] if x != max_value]

if max_value % other_values[0] == 0 & max_value % other_values[1] == 0:
    print('Yes')
else:
    print('No')
    
    