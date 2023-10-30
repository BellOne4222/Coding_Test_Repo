import sys

n, k = map(int, sys.stdin.readline().split())
temperature = list(map(int, sys.stdin.readline().split()))

left = 0
right = 0
result = -100 * k
current_sum = 0

while right < n:
    current_sum += temperature[right]
    if right - left + 1 > k:
        current_sum -= temperature[left]
        left += 1
    result = max(result, current_sum)
    right += 1

print(result)