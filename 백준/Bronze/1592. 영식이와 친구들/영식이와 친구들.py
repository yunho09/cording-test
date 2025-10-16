import sys
N, M, L = map(int, sys.stdin.readline().split())
lis = [0] * (N + 1)
lis[1] += 1
d = 1
count = 0
while max(lis) < M:
  if lis[d] % 2 != 0:
    if d + L <= N:
      d += L
      lis[d] += 1
      count += 1
    else:
      d = (d + L) - N
      lis[d] += 1
      count += 1
  else:
    if d - L > 0:
      d -= L
      lis[d] += 1      
      count += 1
    else:
      d = (d - L) + N
      lis[d] += 1
      count += 1
print(count)