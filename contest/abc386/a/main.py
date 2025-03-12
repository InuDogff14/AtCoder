a,b,c,d = map(int,input().split())

hash_list = set([a,b,c,d])

if len(hash_list) == 2:
    print('Yes')
else:
    print('No')