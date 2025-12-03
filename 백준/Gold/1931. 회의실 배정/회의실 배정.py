import sys
n = int(sys.stdin.readline())
arr = []
count = 1
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))
arr.sort(key=lambda x: x[0])
arr.sort(key=lambda x: x[1])
h = arr[0][1]
del arr[0]
for x in arr:
    if h <= x[0]:
        count += 1
        h = x[1]
print(count)