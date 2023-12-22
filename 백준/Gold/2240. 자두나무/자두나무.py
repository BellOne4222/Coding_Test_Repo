import sys

# 자두가 떨어지는 시간 T와 이동할 수 있는 횟수 W 입력받기
t, w = map(int, sys.stdin.readline().rstrip().split(" "))

# 각 시간에 떨어지는 나무의 번호를 리스트에 저장 (인덱스 0은 사용하지 않음)
arr = [0]
for _ in range(t):
    arr.append(int(sys.stdin.readline()))

# DP 테이블 초기화
dp = [[0] * (w + 1) for _ in range(t + 1)]

for i in range(t + 1):
    # 1번 나무에서 움직이지 않을 경우 처리
    if arr[i] == 1:
        dp[i][0] = dp[i - 1][0] + 1
    else:
        dp[i][0] = dp[i - 1][0]

    for j in range(1, w + 1):
        if (arr[i] == 2 and j % 2 == 1):
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + 1
        elif (arr[i] == 1 and j % 2 == 0):
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + 1
        else:
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j])

# DP 테이블의 마지막 행에서 최대값 출력
print(max(dp[t]))