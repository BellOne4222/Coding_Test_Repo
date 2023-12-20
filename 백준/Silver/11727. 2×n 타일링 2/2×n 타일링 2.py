import sys

n = int(sys.stdin.readline())
dp_table = [0] * 1001

# 초기값 지정
dp_table[0] = 1
dp_table[1] = 1

# 점화식에 따른 경우의 수 계산
for i in range(2, n+1):
    dp_table[i] = dp_table[i-1] + 2 * dp_table[i-2]

print(dp_table[n]%10007)