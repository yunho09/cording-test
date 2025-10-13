import sys
a = int(sys.stdin.readline())
e = []
for _ in range(a):
  b = sys.stdin.readline().strip()
  e.append(b)
e = list(set(e))
e.sort()
e.sort(key=len)
for c in e:
  print(c)