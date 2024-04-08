import sys

# 입력을 더 빠르게 받기 위해 sys.stdin.readline을 사용
input = sys.stdin.readline

# dp[n][k][l]을 사용하여, 길이가 n이며, 인접한 비트의 개수가 k이고, 마지막 비트가 l인 수열의 개수를 저장
dp = [[[0 for _ in range(2)] for _ in range(101)] for _ in range(101)]
dp[1][0][0] = 1  # 길이가 1이고, 인접한 비트가 0개이며, 마지막 비트가 0인 수열의 개수는 1
dp[1][0][1] = 1  # 길이가 1이고, 인접한 비트가 0개이며, 마지막 비트가 1인 수열의 개수도 1

# DP 배열을 채움
for k in range(101):  # 인접한 비트의 개수
    for n in range(2, 101):  # 수열의 길이
        if k == 0:
            dp[n][k][1] = dp[n-1][k][0]  # 마지막이 1로 끝나며, 인접한 비트가 없는 경우는 이전의 마지막이 0인 경우만 해당
        else:
            # 마지막이 1로 끝나며, 인접한 비트가 k개 있는 경우는,
            # 이전에 1로 끝나고, 인접한 비트가 k-1개 있던 경우와
            # 이전에 0으로 끝나고, 인접한 비트가 k개 있던 경우의 합
            dp[n][k][1] = dp[n-1][k-1][1] + dp[n-1][k][0]
        # 마지막이 0으로 끝나는 경우는, 이전이 0 또는 1로 끝났든 상관 없이 합산
        dp[n][k][0] = dp[n-1][k][0] + dp[n-1][k][1]

# 테스트 케이스의 개수 T를 입력받음
T = int(input())
results = []
for _ in range(T):
    N, K = map(int, input().split())  # 각 테스트 케이스에 대한 n과 k 값을 입력받음
    result = dp[N][K][0] + dp[N][K][1]  # 길이가 N이고, 인접한 비트의 개수가 K인 수열의 총 개수를 계산
    results.append(result)  # 결과를 results 리스트에 추가

# 결과를 출력
print('\n'.join(map(str, results)))