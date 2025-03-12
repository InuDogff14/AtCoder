import sys

input = sys.stdin.read
data = input().splitlines()

N,M = map(int(data[0].split))
S = [list(map(int, line.split())) for line in data[1:N+1]]
T = [list(map(int, line.split())) for line in data[N+1:M+1]]