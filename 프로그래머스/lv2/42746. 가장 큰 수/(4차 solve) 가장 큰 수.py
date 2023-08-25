# 4. [0,0,0,0] 반례를 해결하기 위해 만든 result를 정수로 바꿔주고 다시 문자열로 바꾸는 작업 수행해서 반례 해결

def solution(numbers):
    numbers_str = list(map(str, numbers)) # 모든 원소를 map을 이용해서 문자열로 바꿔준다.
    numbers_str.sort(key = lambda x : x*3, reverse = True) # 각 원소를 3번씩 반복한 문자열로 바꿔서 내림차 순으로 정렬
    # [3, 30, 34, 5, 9] -> [333, 303030, 343434, 555, 999]
    
    result = ''
    
    for l in range(len(numbers)): # 빈 문자열에 더해서 결과를 반환하고, 결과는 정수로 한번, 다시 문자열로 바꿔서 반환
        result += numbers_str[l]
        
    result = int(result)
    
    result = str(result)
    
    
    return result
    
    
    
    
        
        
    
    
        