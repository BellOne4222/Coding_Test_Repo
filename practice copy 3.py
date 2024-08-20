import sys
input = sys.stdin.readline

n, m = map(int, input().split())
k = int(input())

# 1. 공사 중인 도로 리스트 생성
construction = [[[] for _ in range(m+1)] for _ in range(n+1)]
for _ in range(k) :
    a, b, c, d = map(int, input().split())
    construction[a][b].append((c, d))
    construction[c][d].append((a, b))
# 2. dp 생성
dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
# 3. 초기값 설정
dp[0][0] = 1
# 4.
for i in range(n+1) :
    for j in range(m+1) :
        # 4-1. 현재 위치의 위쪽이 맵을 벗어나지 않으면서 공사 중인 도로가 아닐 경우
        if i-1 >= 0 and (i-1, j) not in construction[i][j] :
            dp[i][j] += dp[i-1][j]

        # 4-2. 현재 위치의 왼쪽이 맵을 벗어나지 않으면서 공사 중인 도로가 아닐 경우
        if j-1 >= 0 and (i, j-1) not in construction[i][j] :
            dp[i][j] += dp[i][j-1]
# 5. 결과 출력
print(dp[-1][-1])