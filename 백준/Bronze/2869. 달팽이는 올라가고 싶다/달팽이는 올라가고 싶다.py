import sys
a,b,c = map(int, sys.stdin.readline().split())
count = 0
c = c-a
count = c // (a-b)
if c % (a-b) != 0:
  count = count + 1
sys.stdout.write(str(count + 1))