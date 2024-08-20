import sys

# 입력받는 포도주 잔의 개수
n = int(sys.stdin.readline())

# 포도주 양을 저장할 리스트 (최대 10000잔까지 가능)
grapes = [0] * 10001

# 각 포도주 잔의 양을 입력받아 저장
for i in range(1, n + 1):
    grapes[i] = int(sys.stdin.readline())

# DP 테이블 초기화 (포도주 잔의 최대 양을 저장할 테이블)
dp_table = [0] * 10001

# 첫 번째 잔을 마셨을 때의 최대 포도주 양
dp_table[1] = grapes[1]

# 두 번째 잔까지의 최대 포도주 양 (첫 번째 잔과 두 번째 잔을 모두 마심)
if n > 1:
    dp_table[2] = grapes[1] + grapes[2]

# 세 번째 잔부터 마지막 잔까지의 최대 포도주 양을 계산
for i in range(3, n + 1):
    # i번째 잔까지 최대 포도주 양을 구하는 세 가지 경우
    # 1. i번째 잔을 마시지 않는 경우: dp_table[i-1]
    # 2. i번째 잔을 마시고, i-1번째 잔을 마시지 않은 경우: dp_table[i-2] + grapes[i]
    # 3. i번째 잔과 i-1번째 잔을 모두 마시고, i-2번째 잔을 마시지 않은 경우: dp_table[i-3] + grapes[i-1] + grapes[i]
    dp_table[i] = max(dp_table[i - 1], dp_table[i - 2] + grapes[i], dp_table[i - 3] + grapes[i - 1] + grapes[i])

# n번째 잔까지 마실 수 있는 최대 포도주 양 출력
print(dp_table[n])
