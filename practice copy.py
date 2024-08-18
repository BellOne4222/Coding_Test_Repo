import sys

t = int(sys.stdin.readline())

stairs = [0] * (t + 1)

for i in range(1, t + 1):
    stair = int(sys.stdin.readline())
    stairs[i] = stair

dp_table = [0 for _ in range(t + 1)]

dp_table[1] = stairs[1]
dp_table[2] = stairs[1] + stairs[2]
dp_table[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])

for i in range(4, t + 1):
    dp_table[i] = max(dp_table[i - 3] + stairs[i - 1] + stairs[i], dp_table[i - 2] + stairs[i])

print(dp_table[t])