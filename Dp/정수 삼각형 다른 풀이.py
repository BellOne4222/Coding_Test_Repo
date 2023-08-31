# 이것이 취업을 위한 코딩테스트다 p.376 정수 삼각형
# 내려오는 방법 - 1. 왼쪽 위 2. 바로 위 둘중에서 합의 최대 선택해서 dp에 저장
# dp[i][j] = array[i][j] + max(dp[i-1][j-1], dp[i-1][j])


n = 5

dp = [[7],[3,8],[8,1,0],[2,7,4,4],[4,5,2,6,5]]

for i in range(1,n):
    for j in range(i+1):
        # 왼쪽 위에서 내려오는 경우
        if j == 0:
            up_left = 0
        else:
            up_left = dp[i-1][j-1]
        
        if j == i:
            up = 0
        else:
            up = dp[i-1][j]
        
        dp[i][j] = dp[i][j] + max(up_left,up)

print(max(dp[n-1]))

