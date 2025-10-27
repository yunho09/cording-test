import sys
x = int(sys.stdin.readline())
num = 666
count = 0
while count != x:
  if '666' in str(num):
    count += 1
  num += 1
print(num - 1)