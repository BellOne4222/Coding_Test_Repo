import sys


N = int(input())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()
good = 0

for i in range(N):
    parts = nums[:i] + nums[i + 1:]
    l_idx = 0
    r_idx = len(parts) - 1
    while l_idx < r_idx:
        compare = parts[l_idx] + parts[r_idx]
        if compare == nums[i]:
            good += 1
            break
        if compare < nums[i]:
            l_idx += 1 # t 를 증가시켜야 하므로 l_idx 증가
        else:
            r_idx -= 1 # t 를 감소시켜야 하므로 r_idx 감소
        
print(good)