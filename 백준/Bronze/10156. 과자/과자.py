import sys
K, N, M = map(int, sys.stdin.readline().split())
a = K * N - M
print(0) if a < 0 else print(a)