def check(ineqs, nums):
    for i in range(len(ineqs)):
        if ineqs[i] == '<' and nums[i] > nums[i + 1]:
            return False
        if ineqs[i] == '>' and nums[i] < nums[i + 1]:
            return False
    return True

def find_numbers(ineqs, k):
    max_num = ""
    min_num = ""
    
    from itertools import permutations
    
    for perm in permutations(range(10), k + 1):
        if check(ineqs, perm):
            num = ''.join(map(str, perm))
            if not max_num or num > max_num:
                max_num = num
            if not min_num or num < min_num:
                min_num = num
    
    return max_num, min_num

# 입력 받기
import sys
input = sys.stdin.read
data = input().split()

k = int(data[0])
inequalities = data[1:]

max_result, min_result = find_numbers(inequalities, k)

print(max_result)
print(min_result)
