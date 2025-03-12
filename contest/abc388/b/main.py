N,D = map(int,input().split())
snakes = [list(map(int, input().split())) for _ in range(N)]

max_weight = 0

for i in range(1,D+1):
    for snake in snakes:
        weight = snake[0] * (snake[1] + i )
        if weight > max_weight:
            max_weight = weight
        
    print(max_weight)
    max_weight = 0