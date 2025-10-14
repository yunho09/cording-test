import sys
a = int(sys.stdin.readline())
INF = 10**9
dp = [INF] * (a + 1)
dp[0] = 0
for i in range(1, a + 1):
  if i >= 3:
    dp[i] = min(dp[i], dp[i-3] + 1)
  if i >= 5:
    dp[i] = min(dp[i], dp[i-5] + 1)
print(dp[a] if dp[a] < INF else -1)