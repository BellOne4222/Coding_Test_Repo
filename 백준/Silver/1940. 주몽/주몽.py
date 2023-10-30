import sys

n = int(sys.stdin.readline().rstrip())

m = int(sys.stdin.readline().rstrip())

lst = list(map(int, sys.stdin.readline().split()))

lst = sorted(lst) # [1, 2, 3, 4, 5, 7]

left = 0
right = len(lst) - 1
result = 0

while left < right:
    combine = lst[left] + lst[right]
    if combine == m:
        result += 1
        left += 1
    elif combine > m:
        right -= 1
    else:
        left += 1

print(result)