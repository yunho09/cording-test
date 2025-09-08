import sys
a = int(sys.stdin.readline())
b = []
for _ in range(a):
  b.append(int(sys.stdin.readline()))
b.sort()
for i in b:
  print(i)
