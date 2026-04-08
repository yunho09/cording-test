import sys
n = int(sys.stdin.readline())
total = 1000 - n
count = 0
list = [500, 100, 50, 10, 5, 1]
for i in list:
    count += total // i
    total %= i
print(count)