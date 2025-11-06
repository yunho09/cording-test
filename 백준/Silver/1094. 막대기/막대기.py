import sys
x = int(sys.stdin.readline())
arr = [64, 32, 16, 8, 4, 2, 1]
b = 0
count = 0
for i in arr:
  if b + i <= x:
    b += int(i)
    count += 1
  if b == x:
    break
print(count)