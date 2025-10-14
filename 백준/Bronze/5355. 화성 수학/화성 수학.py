import sys
a = int(sys.stdin.readline())
for _ in range(a):
  b = sys.stdin.readline().split()
  for i in b[1:]:
    if str(i) == '@':
      b[0] = float(b[0])*3
    elif str(i) == '%':
      b[0] = float(b[0])+5
    elif str(i) == '#':
      b[0] = float(b[0])-7  
  print(f'{b[0]:.2f}') 
  b.clear