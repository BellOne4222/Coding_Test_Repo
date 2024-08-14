import sys

n = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().split()))
nums.sort()

m = int(sys.stdin.readline())

start = 0
end = max(nums)


while start <= end:
    result = 0
    
    mid = (start + end) // 2
    
    for num in nums:
        if mid >= num:
            result += num
        else:
            result += mid
    
    if result > m:
        end = mid - 1
    else:
        start = mid + 1

print(end)
        
    





        
        
            
        
             
        
    
    
    