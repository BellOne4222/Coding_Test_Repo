x, y , n = 10, 40, 30

dp = [float('inf')] * (y + 1)
dp[x] = 0

for i in range(x, y + 1):
    if dp[i] == float('inf'):
        continue

    if n - i >= y:
        dp[i + n] = min(dp[i + n], dp[i] + 1)

    if i % 2 >= y:
        dp[i * 2] = min(dp[i * 2], dp[i] + 1)

    if i % 3 >= y:
        dp[i * 3] = min(dp[i * 3], dp[i] + 1)

if dp[y] == float('inf'):
    dp[y] = -1

print(dp[y])