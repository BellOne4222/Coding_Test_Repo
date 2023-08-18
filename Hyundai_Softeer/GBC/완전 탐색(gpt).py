def find_max_exceeded_speed(N, M, limits, tests):
    max_exceeded_speed = 0

    for i in range(M):
        test_length, test_speed = tests[i]
        total_length = 0

        for j in range(N):
            limit_length, limit_speed = limits[j]

            # 현재 구간의 길이만큼 추가
            total_length += limit_length

            # 테스트 구간에 도달하면 비교
            if total_length >= test_length:
                exceeded_speed = test_speed - limit_speed

                # 제한 속도를 초과한 경우에만 최댓값 갱신
                if exceeded_speed > max_exceeded_speed:
                    max_exceeded_speed = exceeded_speed
                break

    return max_exceeded_speed

# 입력 예제
N, M = map(int, input().split())
limits = [list(map(int, input().split())) for _ in range(N)]
tests = [list(map(int, input().split())) for _ in range(M)]

result = find_max_exceeded_speed(N, M, limits, tests)
print(result)

# 이 풀이에서는 입력된 구간과 테스트 구간을 하나씩 비교하여 제한 속도를 초과한 값을 찾습니다. 각 구간별로 제한 속도를 계산하고 실제 속도와 비교하여 차이가 가장 큰 값을 찾아냅니다. 이를 위해 루프를 사용하여 구간을 순회하고, 각 구간에서의 제한 속도와 실제 속도의 차이를 계산합니다.
