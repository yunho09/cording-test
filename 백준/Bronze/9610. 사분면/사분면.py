import sys
a = int(sys.stdin.readline())
list = [0] * 5
for i in range(a):
  x, y = map(int, sys.stdin.readline().split())
  if x > 0 and y > 0:
    list[0] += 1
  elif x < 0 and y > 0:
    list[1] += 1
  elif x < 0 and y < 0:
    list[2] += 1
  elif x > 0 and y < 0:
    list[3] += 1
  else:
    list[4] += 1
print(f'Q1: {list[0]}')
print(f'Q2: {list[1]}')
print(f'Q3: {list[2]}')
print(f'Q4: {list[3]}')
print(f'AXIS: {list[4]}')