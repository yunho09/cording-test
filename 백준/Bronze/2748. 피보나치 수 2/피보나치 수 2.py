import sys
n = int(sys.stdin.readline())
lis = [0] * (n + 1)
lis[1] = 1
for i in range(2, n + 1):
  lis[i] = lis[i - 1] + lis[i - 2]
print(lis[n])


