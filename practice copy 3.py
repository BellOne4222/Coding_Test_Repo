import sys

n, k = map(int, sys.stdin.readline().split())

dp_table = [1] * (n+1)
for i in range(2, k+1):    
    for j in range(1, n+1):
        dp_table[j] += dp_table[j-1]

result = dp_table[n]
print(result % 1000000000)