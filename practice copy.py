import sys

n = int(sys.stdin.readline())

boxes = list(map(int, sys.stdin.readline().split()))

dp_table = [1] * n

for i in range(n):
    for j in range(i):
        if boxes[i] > boxes[j]:
            dp_table[i] = max(dp_table[i], dp_table[j] + 1)

print(max(dp_table))
    
