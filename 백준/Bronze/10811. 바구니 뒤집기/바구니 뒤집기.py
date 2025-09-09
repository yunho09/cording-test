import sys
a, b = map(int, sys.stdin.readline().split())
c = list(range(1,a+1))
for _ in range(b):
  i, j = map(int, sys.stdin.readline().split())
  c[i-1:j] = c[i-1:j][::-1]
for i in c:
  print(i)