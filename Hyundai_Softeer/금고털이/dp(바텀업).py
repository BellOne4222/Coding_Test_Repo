def knapsack(W, weights, values, n):
    # dp[i][j]: i번째 귀금속까지 고려하고 배낭의 무게가 j일 때의 최대 가격
    dp = [[0] * (W+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(1, W+1):
            # 현재 귀금속을 배낭에 넣을 수 있는 경우와 넣을 수 없는 경우를 각각 계산하여 더 큰 값을 저장
            if weights[i-1] <= j:
                dp[i][j] = max(values[i-1] + dp[i-1][j-weights[i-1]], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    
    return dp[n][W]


# 입력 받기
W, N = map(int, input().split())
weights = []
values = []
for _ in range(N):
    weight, value = map(int, input().split())
    weights.append(weight)
    values.append(value)

# 함수 호출 및 결과 출력
result = knapsack(W, weights, values, N)
print(result)



#  세 번째 버전은 반복문을 활용하여 작은 부분 문제부터 해결해 나가는 바텀업 방식입니다. 
