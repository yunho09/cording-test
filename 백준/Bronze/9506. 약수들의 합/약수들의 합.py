import sys
b = 0
while 1:
  b = int(sys.stdin.readline())
  if b == -1:
    break
  list = []
  for i in range(1, b):
    if b % i == 0: 
      list.append(i)
  if sum(list) == b:
    print(f'{b} = {' + '.join(map(str, list))}')
  else:
      print(f'{b} is NOT perfect.')