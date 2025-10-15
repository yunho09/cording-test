import sys
a, b = map(int, sys.stdin.readline().split())
c = list(map(int, sys.stdin.readline().split()))
i = 0
c.sort()
while i < len(c):
  if b >= c[i]:
    b = b + 1
    i = i + 1
  else:
    break
print(b)