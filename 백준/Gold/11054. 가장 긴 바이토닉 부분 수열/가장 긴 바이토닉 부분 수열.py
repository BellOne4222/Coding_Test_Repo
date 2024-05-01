import sys

# Read input
n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().split()))

# DP tables for increasing and decreasing subsequences
increase = [1] * n
decrease = [1] * n

# Calculate longest increasing subsequence length for each position
for i in range(n):
    for j in range(i):
        if a[j] < a[i]:
            increase[i] = max(increase[i], increase[j] + 1)

# Calculate longest decreasing subsequence length for each position
for i in reversed(range(n)):
    for j in range(i + 1, n):
        if a[j] < a[i]:
            decrease[i] = max(decrease[i], decrease[j] + 1)

# Calculate the maximum length of the bitonic subsequence
max_length = 0
for i in range(n):
    max_length = max(max_length, increase[i] + decrease[i] - 1)

print(max_length)
