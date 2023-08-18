def find_max_exceeded_speed(N, M, limits, tests):
    max_exceeded_speed = 0
    cumulative_lengths = [0]

    # 각 구간의 누적 길이 계산
    for i in range(N):
        limit_length, _ = limits[i]
        cumulative_lengths.append(cumulative_lengths[-1] + limit_length)

    # 테스트 구간에서의 제한 속도를 초과한 값 탐색
    for i in range(M):
        test_length, test_speed = tests[i]
        left = 0
        right = len(cumulative_lengths) - 1

        while left < right:
            mid = (left + right) // 2

            if cumulative_lengths[mid] < test_length:
                left = mid + 1
            else:
                right = mid

        # 실제 길이와 제한 속도를 비교하여 최댓값 갱신
        limit_speed = limits[left][1]
        exceeded_speed = test_speed - limit_speed

        if exceeded_speed > max_exceeded_speed:
            max_exceeded_speed = exceeded_speed

    return max_exceeded_speed

# 입력 예제
N, M = map(int, input().split())
limits = [list(map(int, input().split())) for _ in range(N)]
tests = [list(map(int, input().split())) for _ in range(M)]

result = find_max_exceeded_speed(N, M, limits, tests)
print(result)

# 이 풀이에서는 제한 속도를 초과한 값이 나타날 수 있는 위치를 이진 탐색을 통해 찾습니다. 각 구간의 누적 길이를 계산한 후, 테스트 구간에서의 실제 길이를 찾을 때까지 이진 탐색을 수행합니다. 이를 통해 제한 속도를 초과한 값을 찾아냅니다.
