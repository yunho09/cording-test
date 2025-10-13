import sys
a = int(sys.stdin.readline())
e = []
for _ in range(a):
  b,c = sys.stdin.readline().split()
  b = int(b)
  e.append([b,c])
e.sort(key=lambda x:x[0])
for b,c in e:
  print(b,c)