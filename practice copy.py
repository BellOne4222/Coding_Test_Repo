import sys
from itertools import combinations

N, S = map(int, sys.stdin.readline().split())

nums = list(map(int, sys.stdin.readline().split()))

cnt = 0

for i in range(1, N+1):
    comb_nums = list(combinations(nums, i))
    
    for j in comb_nums:
        if len(j) < 0:
            continue
        else:
            if sum(j) == S:
                cnt += 1

print(cnt)


