days = list(map(int,input().split()))
n = max(days)
days = set(days)
dp = [0] * (n + 1)
for i in range(1, n + 1):
    if i in days:
        if i >= 30:
            dp[i] = min(dp[i - 1] + 2, dp[i - 7] + 7, dp[i - 30] + 25)
        elif i >= 7:
            dp[i] = min(dp[i - 1] + 2, dp[i - 7] + 7, 25)
        else:
            dp[i] = min(dp[i - 1] + 2, 7)
    else:
        dp[i] = dp[i - 1]
print(dp[n])