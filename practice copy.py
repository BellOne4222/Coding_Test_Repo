# 시간 복잡도 : O(N)

import sys

# 입력으로 n과 k를 읽어옵니다.
n, k = map(int, sys.stdin.readline().split())

# 온도 값을 입력으로 받아 리스트에 저장합니다.
temperature = list(map(int, sys.stdin.readline().split()))

# 초기 온도 합을 설정합니다.
current_temperature = sum(temperature[:k])

# 최대 온도 합을 추적하는 변수를 초기화합니다.
max_sum = current_temperature

# 연속적인 K일의 온도 합을 찾는 반복문
for i in range(k, n):
    # 슬라이딩 윈도우를 사용하여 현재 날짜의 온도를 더하고 이전 K일의 온도를 빼서 합을 업데이트합니다.
    current_temperature = current_temperature - temperature[i - k] + temperature[i]
    
    # max 함수를 사용하여 현재까지의 최대 온도 합과 새로 계산한 온도 합 중 더 큰 값을 선택하여 max_sum에 저장합니다.
    max_sum = max(max_sum, current_temperature)

# for 루프가 끝나면 최대 온도 합인 max_sum을 출력합니다.
print(max_sum)