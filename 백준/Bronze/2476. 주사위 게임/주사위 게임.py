import sys
x = int(sys.stdin.readline())
m = []
for _ in range(x):
  a, b, c = map(int, sys.stdin.readline().split())
  if a == b == c:
    m.append(10000+a*1000)
  elif a == b:
    m.append(1000+a*100)
  elif a == c:
    m.append(1000+a*100)
  elif c == b:
    m.append(1000+b*100)
  else:
    m.append(max(a,b,c)*100)
print(max(m))