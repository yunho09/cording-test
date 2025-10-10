import sys
arr = []
for _ in range(7):
  a = int(sys.stdin.readline())
  arr.append(a)
if any(a % 2 == 1 for a in arr):
  print(sum(b for b in arr if b % 2 == 1))
  print(min(b for b in arr if b % 2 == 1))
else:
  print('-1')