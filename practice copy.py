import sys
from itertools import permutations

nums = []

for _ in range(5):
    nums += sys.stdin.readline().split()

comb_nums = list(permutations(nums, 6))

comb_nums = set(comb_nums)

print(comb_nums)


