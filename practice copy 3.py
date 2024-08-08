import sys
from itertools import permutations

k = int(sys.stdin.readline())

inequalitys = list(map(str, sys.stdin.readline().split()))

nums = [i for i in range(10)]

comb_nums = list(permutations(nums, k+1))

print(comb_nums[:10])