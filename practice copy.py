n = 11

nums = ["1", "2", "4"]

ans = ""

while n > 0:
    n = n - 1
    ans = nums[n%3] + ans
    n //= 3

print(ans)
    
    
    