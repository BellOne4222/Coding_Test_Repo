def knapsack(W, weights, values, n):
    # 기저 사례: 배낭의 무게가 0이거나 모든 귀금속을 확인한 경우
    if W == 0 or n == 0:
        return 0
    
    # 배낭에 담을 수 있는 귀금속인 경우와 담을 수 없는 경우를 각각 계산하여 더 큰 값을 반환
    if weights[n-1] <= W:
        return max(values[n-1] + knapsack(W-weights[n-1], weights, values, n-1),
                   knapsack(W, weights, values, n-1))
    else:
        return knapsack(W, weights, values, n-1)


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

# 첫 번째 버전은 재귀 함수를 활용하여 모든 경우를 탐색하는 완전 탐색 방식입니다.