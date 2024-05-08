import sys

n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().split()))

increase = [1] * n
decrease = [1] * n


for i in range(n):
    for j in range(i):
        if a[j] < a[i]:
            increase[i] = max(increase[i], increase[j] + 1)

for i in reversed(range(n)):
    for j in range(i + 1, n):
        if a[j] < a[i]:
            decrease[i] = max(decrease[i], decrease[j] + 1)

max_length = 0
for i in range(n):
    max_length = max(max_length, increase[i] + decrease[i] - 1)

print(max_length)