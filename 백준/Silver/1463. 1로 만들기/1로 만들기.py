import sys
n = int(sys.stdin.readline())
lis = [0] * (n + 1)
lis[1] = 0
for i in range(2, n + 1):
  lis[i] = lis[i-1] + 1
  if i%2==0:
    lis[i] = min(lis[i//2] + 1, lis[i])
  if i%3==0:
    lis[i] = min(lis[i//3] + 1, lis[i])
print(lis[n])

