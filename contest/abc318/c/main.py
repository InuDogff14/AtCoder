import heapq

n,d,p = map(int,input().split())

f = list(map(int,input().split()))

nums = heapq.nlargest(d,f)