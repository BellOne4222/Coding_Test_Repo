import sys

code = list(map(int, sys.stdin.readline().rstrip())) # [2, 5, 1, 1, 4]

case = 2

idx_cases = []

for i in range(len(code) - 1):
    cur_idx = [i,i+1]
    
    if cur_idx not in idx_case:
        idx_cases.append(cur_idx)
        