import sys
T = int(sys.stdin.readline())
stair = [0]
dp = []
for i in range(T):
    stair.append(int(sys.stdin.readline()))
dp.append(0)
dp.append(stair[1])
if T > 1:
    dp.append(stair[1] + stair[2])
    for i in range(3, T+1):
        dp.append(max((dp[i-3]+stair[i-1]+stair[i]), dp[i-2]+stair[i]))
print(dp[-1])