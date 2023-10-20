import sys
from collections import deque
import itertools

n = int(sys.stdin.readline().rstrip())

nums = list(map(int,sys.stdin.readline().split()))
nums = sorted(nums)

good = 0


nums = deque(nums)

cnt = 1
parts = []
candidations = []
sums = []

while True:
    if cnt > n:
        break
    parts = []
    compare = nums.popleft()
    part = sum(1 for item in nums if compare > item)
    if part >= 2:
        for i in nums:
            if compare > i:
                parts.append(i)
        candidations = list(itertools.combinations(parts,2))
        for j in range(len(candidations)):
            s = candidations[j][0] + candidations[j][1]
            if s == compare:
                good += 1
                break
        nums.append(compare)
    else:
        nums.append(compare)
    

print(good)
