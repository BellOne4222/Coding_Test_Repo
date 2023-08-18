def knapsack(W, weights, values, n, memo):
    # 기저 사례: 배낭의 무게가 0이거나 모든 귀금속을 확인한 경우
    if W == 0 or n == 0:
        return 0
    
    # 이미 계산한 값이 있는 경우 해당 값 반환
    if memo[W][n] != -1:
        return memo[W][n]
    
    # 배낭에 담을 수 있는 귀금속인 경우와 담을 수 없는 경우를 각각 계산하여 더 큰 값을 저장
    if weights[n-1] <= W:
        memo[W][n] = max(values[n-1] + knapsack(W-weights[n-1], weights, values, n-1, memo),
                         knapsack(W, weights, values, n-1, memo))
    else:
        memo[W][n] = knapsack(W, weights, values, n-1, memo)
    
    return memo[W][n]


# 입력 받기
W, N = map(int, input().split())
weights = []
values = []
for _ in range(N):
    weight, value = map(int, input().split())
    weights.append(weight)
    values.append(value)

# 메모이제이션을 위한 memo 배열 초기화
memo = [[-1] * (N+1) for _ in range(W+1)]

# 함수 호출 및 결과 출력
result = knapsack(W, weights, values, N, memo)
print(result)

#  두 번째 버전은 동적 계획법을 활용하여 중복 계산을 피하고 메모이제이션을 사용하는 탑다운 방식입니다