import sys

# 입력 받기
n, k = map(int, sys.stdin.readline().split())

# DP 테이블 초기화: 0부터 N까지의 합이 되는 경우의 수를 저장할 배열
dp_table = [1] * (n+1)

# 2부터 K까지 반복
for i in range(2, k+1):
    # 1부터 N까지의 경우의 수를 계산하는 과정
    for j in range(1, n+1):
        # 현재 수의 경우의 수는 이전 수의 경우의 수들의 합과 같다.
        dp_table[j] += dp_table[j-1]

# 최종 결과: N을 만드는 경우의 수
result = dp_table[n]

# 결과 출력 (1,000,000,000으로 나눈 나머지)
print(result % 1000000000)