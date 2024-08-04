import sys

n = int(sys.stdin.readline())

n_nums = list(map(int, sys.stdin.readline().rstrip().split()))

m = int(sys.stdin.readline())

num_cards = list(map(int, sys.stdin.readline().rstrip().split()))

n_nums.sort()

answer = []

for card in num_cards:
    target = card
    left = 0
    right = n-1
    flag = False
    
    while left <= right:
        mid_idx = (left + right) // 2
        
        if n_nums[mid_idx] == target:
            answer.append(1)
            flag = True
            break
        
        elif n_nums[mid_idx] > target:
            right = mid_idx - 1
        
        else:
            left = mid_idx + 1
    
    if not flag:
        answer.append(0)
    

print(" ".join(map(str, answer)))        
        