def solution(n, times):
    min_time = 0  # 최소 시간을 초기화합니다.

    left = times[0]  # 가장 짧은 심사 시간을 최소 범위로 설정합니다.
    right = times[0] * n  # 가장 긴 심사 시간을 최대 범위로 설정합니다.

    while True:
        mid = (left + right) // 2  # 중간값을 계산합니다.
        waiting = 0  # 현재 중간값에서의 대기 시간을 초기화합니다.

        for i in times:
            waiting += mid // i  # 중간값을 각 심사 시간으로 나누어 대기 시간을 누적합니다.

        if waiting < n:  # 대기 시간이 목표 대기 인원보다 작다면 시간을 늘려야 합니다.
            left = mid + 1  # 중간값보다 큰 범위에서 다시 이분 탐색을 진행합니다.

        elif waiting >= n:  # 대기 시간이 목표 대기 인원 이상이라면 시간을 줄여야 합니다.
            right = mid  # 중간값보다 작은 범위에서 다시 이분 탐색을 진행합니다.

        if left == right - 1:  # 이분 탐색 범위가 1인 경우, 최소 시간을 찾았습니다.
            min_time = right  # 최소 시간을 업데이트하고 반복문을 종료합니다.
            break

    return min_time  # 최소 시간을 반환합니다.