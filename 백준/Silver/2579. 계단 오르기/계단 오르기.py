N = int(input())
stair = [0]
dp = [0]*(N+1)

for i in range(1,N+1):
    stair.append(int(input()))
    if i == 1 :
        dp[1] = stair[1]
    elif i == 2 :
        dp[2] = stair[1] + stair[2]
    else :
        dp[i] = max(stair[i]+stair[i-1]+dp[i-3], stair[i]+dp[i-2])

print(dp[N])
