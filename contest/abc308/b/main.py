n, m = map(int, input().split())  # N, Mの取得
c = list(input().split())
d = list(input().split())
p = list(map(int, input().split()))

price = {'else':p[0]}

i = 1

for kind in d:
    price[kind] = p[i]
    i +=1

# print(price['else'])

result = 0

for color in c:
    if color in price:
        result += price.get(color)
        
    else:
        result += price.get('else')

print(result)