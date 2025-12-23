import sys
n = int(sys.stdin.readline())
nlist = []
dp = [0] * 12
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(n):
     nlist.append(int(sys.stdin.readline()))
for i in range(max(nlist)+1):
    if i == 1 or i == 2 or i == 3:
        continue
    else:
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
for i in nlist:
    print(dp[i], end='\n')
