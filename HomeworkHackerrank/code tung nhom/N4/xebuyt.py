days = [int(x) for x in input().split()]

ticket_value = [2, 7, 25]

def getResult(days):
    dp = [0 for i in range(0, days[-1]+1)]
    for i in range(days[-1] + 1):
        if i in days:
            dp[i] = min(ticket_value[0] + dp[i-1], \
                        ticket_value[1] + (0 if i < 7 else dp[i -7]), \
                        ticket_value[2] + (0 if i < 30 else dp[i-30]))
        else:
            dp[i] = dp[i - 1]
    return dp[-1]

print(getResult(days))