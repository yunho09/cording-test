import sys
n = int(sys.stdin.readline())
a = []
for _ in range(n):
  a.append(int(sys.stdin.readline()))
a = sorted(a)
for i in range(n):
  sys.stdout.write(str(a[i]) + '\n')