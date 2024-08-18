import sys

n = int(sys.stdin.readline())

a = list(map(int, sys.stdin.readline().split()))

dp_table = [1] * 1001

for i in range(n):
    for j in range(i):
        if a[i] < a[j]:
            dp_table[i] = max(dp_table[i], dp_table[j] + 1)

print(max(dp_table))