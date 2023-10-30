import sys

n, k = map(int, sys.stdin.readline().split())
temperature = list(map(int, sys.stdin.readline().split()))

# 초기 온도의 합을 설정
current_temperature = sum(temperature[:k])
max_sum = current_temperature

for i in range(k, n):
    # 이전 K일의 온도 합에서 현재 날짜의 온도를 뺀 후, 다음 날짜의 온도를 더함 (슬라이딩 윈도우)
    current_temperature = current_temperature - temperature[i - k] + temperature[i]
    max_sum = max(max_sum, current_temperature)

print(max_sum)