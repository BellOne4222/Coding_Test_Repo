import sys

# 입력된 계단의 개수를 읽어옵니다.
t = int(sys.stdin.readline())

# 계단의 점수를 저장할 리스트를 초기화합니다.
# 계단 수는 최대 300개이므로, 301개의 요소를 가진 리스트를 생성합니다.
stairs = [0] * 301

# 계단의 점수를 입력받아 리스트에 저장합니다.
for i in range(1, t + 1):
    stair = int(sys.stdin.readline())
    stairs[i] = stair

# 최대 점수를 저장할 DP(동적 프로그래밍) 테이블을 초기화합니다.
# 역시 계단 수는 최대 300개이므로, 301개의 요소를 가진 리스트를 생성합니다.
dp_table = [0] * 301

# 기본 상태를 설정합니다.
# dp_table[1]은 첫 번째 계단을 밟는 경우의 최대 점수입니다.
dp_table[1] = stairs[1]

# dp_table[2]는 첫 번째 계단과 두 번째 계단을 연속으로 밟는 경우의 최대 점수입니다.
dp_table[2] = stairs[1] + stairs[2]

# dp_table[3]은 첫 번째 계단과 세 번째 계단을 밟는 경우와
# 두 번째 계단과 세 번째 계단을 밟는 경우 중 큰 점수를 선택합니다.
dp_table[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])

# 4번째 계단부터 t번째 계단까지의 최대 점수를 계산합니다.
for i in range(4, t + 1):
    # 현재 계단 i를 밟는 경우의 최대 점수를 계산합니다.
    # 두 가지 경우를 고려합니다:
    # 1. i-3 번째 계단까지 밟은 후 i-1 번째 계단과 현재 i 번째 계단을 밟는 경우
    # 2. i-2 번째 계단까지 밟은 후 현재 i 번째 계단을 밟는 경우
    dp_table[i] = max(dp_table[i - 3] + stairs[i - 1] + stairs[i], dp_table[i - 2] + stairs[i])

# t번째 계단까지 도달할 때의 최대 점수를 출력합니다.
print(dp_table[t])
