def check(a, b, c): # 소수 판별
    total = a + b + c
    for i in range(2, total): 
        if total % i == 0 :
            return False 
    return True 

def solution(nums):
    result = 0
    for i in range(0, len(nums) - 2): # 삼중 반복문으로 숫자들 중 3개 뽑는 로직 구현
        for j in range(i+1, len(nums) - 1): 
            for k in range(j+1, len(nums)): 
                if check(nums[i], nums[j], nums[k]): # 뽑은 숫자들의 합을 소수 판별해서 true 이면 result 1증가
                    result += 1
    return result
    