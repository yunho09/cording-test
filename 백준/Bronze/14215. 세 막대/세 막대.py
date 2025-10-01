import sys
a, b, c = map(int, sys.stdin.readline().split())
d = max(a,b,c)
e = a + b + c - d
if d < e:
  sys.stdout.write(str(e + d))
else:
  sys.stdout.write(str(2 * e - 1))