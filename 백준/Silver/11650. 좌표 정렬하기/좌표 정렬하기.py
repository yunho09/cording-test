import sys
n = int(sys.stdin.readline())
numlist = []
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    numlist.append([a, b])
numlist.sort(key=lambda x : (x[0], x[1]))
for i in numlist:
    print(i[0], i[1])