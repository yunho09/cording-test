import sys
a = int(sys.stdin.readline())
b = 0
c = 1
while True:
  if b + c <= a:
    b = b + c
    c = c + 1
  else:
    break
print(c - 1)