def main():
    dp = [[[0 for _ in range(2)] for _ in range(101)] for _ in range(101)]
    dp[1][0][0] = 1
    dp[1][0][1] = 1

    for k in range(101):
        for n in range(2, 101):
            if k == 0:
                dp[n][k][1] = dp[n-1][k][0]
            else:
                dp[n][k][1] = dp[n-1][k-1][1] + dp[n-1][k][0]
            dp[n][k][0] = dp[n-1][k][0] + dp[n-1][k][1]

    T = int(input())
    results = []
    for _ in range(T):
        N, K = map(int, input().split())
        result = dp[N][K][0] + dp[N][K][1]
        results.append(result)

    # Print all results at once, separated by newlines.
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()