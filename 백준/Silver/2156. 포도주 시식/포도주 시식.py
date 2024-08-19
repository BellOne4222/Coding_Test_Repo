import sys

n = int(sys.stdin.readline())

grapes = [0] * 10001

for i in range(1, n + 1):
    grapes[i] = int(sys.stdin.readline())

dp_table = [0] * 10001

dp_table[1] = grapes[1]
if n > 1:
    dp_table[2] = grapes[1] + grapes[2]

for i in range(3, n + 1):
    dp_table[i] = max(dp_table[i - 1], dp_table[i - 2] + grapes[i], dp_table[i - 3] + grapes[i - 1] + grapes[i])

print(dp_table[n])
