import sys

n = int(sys.stdin.readline())

dp_table = [0] * 91

dp_table[0] = 0
dp_table[1] = 1

for i in range(2,n+1):
    dp_table[i] = dp_table[i-1] + dp_table[i-2]

print(dp_table[n])