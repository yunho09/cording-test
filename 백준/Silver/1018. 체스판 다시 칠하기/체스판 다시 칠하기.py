import sys
wblist = []
n, m = map(int, sys.stdin.readline().split())
num = 64
for i in range(n):
    wblist.append(sys.stdin.readline().strip())
for i in range(n-7):
    for j in range(m-7):
        numWB = 0
        numBW = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k + l) % 2 == 0:
                    if wblist[k][l] != 'W':
                        numWB += 1
                else:
                    if wblist[k][l] != 'B':
                        numWB += 1
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k + l) % 2 == 0:
                    if wblist[k][l] != 'B':
                        numBW += 1
                else:
                    if wblist[k][l] != 'W':
                        numBW += 1
        num = min(min(numWB, numBW), num)
print(num)