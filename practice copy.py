import sys
from collections import deque

k = int(sys.stdin.readline())

inequalitys = list(map(str, sys.stdin.readline().split()))

max_answer = []
min_answer = []

max_nums = [i for i in reversed(range(10))]

min_nums = [j for j in range(10)]
max_idx = 0
min_idx = 0
i_idx = 0

compare = deque()

while len(max_answer) < k+1:
    if max_idx == 0 and i_idx == 0:
        if inequalitys[i_idx] == "<":
            pass
        else:
            max_answer.append(max_nums[max_idx])
            max_idx += 1
            i_idx += 1
    
    else:
        if inequalitys[i_idx-1] == "<":
            if inequalitys[i_idx] == "<":
                compare.appendleft(max_nums[max_idx])
                i_idx += 1
                max_idx += 1
            else:
                for num in compare:
                    max_answer.append(num)
                max_answer.append(max_nums[max_idx])
                max_idx += 1
                i_idx += 1
        else:
            if inequalitys[i_idx] == ">":
                max_answer.append(max_nums[max_idx])
                max_idx += 1
                i_idx += 1
            else:
                compare.appendleft(max_nums[max_idx])
                max_idx += 1
                compare.appendleft(max_nums[max_idx])
                i_idx += 1
        

print(max_nums)            
            
            
        
    
