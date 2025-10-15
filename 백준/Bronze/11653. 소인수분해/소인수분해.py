import sys
a = int(sys.stdin.readline())
c = 2
while a > 1:
  while a % c == 0:
    print(c, end='\n')
    a = a//c
  c = c + 1