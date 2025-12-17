import sys
M = int(sys.stdin.readline())
N = int(sys.stdin.readline())
snum = []
for i in range(M, N+1):
    if i < 2:
        continue
    s = True
    for j in range(2, i):
        if i % j == 0:
            s = False
            break
    if s:
        snum.append(i)
if len(snum) == 0:
    print(-1)
else:
    print(sum(snum))
    print(snum[0])