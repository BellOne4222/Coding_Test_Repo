import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())

nums = list(map(int,sys.stdin.readline().split()))
nums = sorted(nums)

nums = deque(nums)
co_nums = [i for i in nums]

l_idx = 0
r_idx = 0
good = 0
idx = 0
for i in range(len(nums)):
    target = co_nums[idx]
    nums.popleft()
    if target == 1:
        nums.appendleft(target)
        idx += 1
        continue
    else:
        r_idx = len(nums) - 1
        while True:
            if nums[r_idx] > target or r_idx == l_idx:
                r_idx -= 1

                
                nums.appendleft(target)
                break
                    
            if nums[l_idx] + nums[r_idx] == target:
                nums.appendleft(target)
                good += 1
                idx += 1
                break
            else:
                if nums[l_idx] + nums[r_idx] > target:
                    r_idx -= 1
                    if r_idx <= 0:
                        nums.appendleft(target)
                        break
                elif nums[l_idx] + nums[r_idx] < target:
                    l_idx += 1
                    if l_idx == r_idx:
                        nums.appendleft(target)
                        break
                

print(good)



