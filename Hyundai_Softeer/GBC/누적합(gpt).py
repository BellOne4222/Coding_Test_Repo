def find_max_exceeded_speed(N, M, limits, tests):
    max_exceeded_speed = 0
    cumulative_limit = 0

    # 각 구간의 누적 제한 속도 계산
    for i in range(N):
        limit_length, limit_speed = limits[i]
        cumulative_limit += limit_speed

    # 테스트 구간에서의 실제 속도와 누적 제한 속도 비교
    for i in range(M):
        test_length, test_speed = tests[i]

        # 제한 속도를 초과한 경우에만 최댓값 갱신
        exceeded_speed = test_speed - cumulative_limit
        if exceeded_speed > max_exceeded_speed:
            max_exceeded_speed = exceeded_speed

    return max_exceeded_speed

# 입력 예제
N, M = map(int, input().split())
limits = [list(map(int, input().split())) for _ in range(N)]
tests = [list(map(int, input().split())) for _ in range(M)]

result = find_max_exceeded_speed(N, M, limits, tests)
print(result)

# 이 풀이에서는 각 구간의 누적 제한 속도를 계산하고, 테스트 구간에서의 실제 속도와 누적 제한 속도를 비교합니다. 이를 통해 제한 속도를 초과한 값을 찾아냅니다. 이를 위해 구간의 길이와 제한 속도를 누적하여 저장한 후, 테스트 구간에서의 실제 속도와 비교합니다