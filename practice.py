from collections import deque

def solution(number, k):
    nums = deque()
    
    for i in range(len(number)):
        
        if len(nums) == 0:
            nums.append(number[i])
            number = number[i+1:]
        elif int(nums[-1]) < int(number[i]):
            nums.popleft()
            nums.append(number[i])
            number = number[i+1:]
            k -= 1
        elif int(nums[-1]) > int(number[i]):
            k -= 1
            number = number[i+1:]
        elif int(nums[-1]) == int(number[i]):
            nums.append(number[i])
            number = number[i+1:]
        if k == 0:
            break

            
    result = ''
    
    for j in nums:
        result += j
    
    return result + number
    
    
        
    
        