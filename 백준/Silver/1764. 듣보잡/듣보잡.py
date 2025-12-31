import sys
n, m = map(int, sys.stdin.readline().split())
dList = []
for _ in range(n+m):
    dList.append(sys.stdin.readline().strip())
oneList = set()
twoList = []
for i in dList:
    if i in oneList:
        twoList.append(i)
    else:
        oneList.add(i)
twoList.sort()
print(len(twoList))
for i in twoList:
    print(i, end='\n')