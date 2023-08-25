def solution(numbers):
    numbers_str = list(map(str, numbers))
    numbers_str.sort(key = lambda x : x*3, reverse = True)
    
    result = ''
    
    for l in range(len(numbers)):
        result += numbers_str[l]
        
    result = int(result)
    
    result = str(result)
    
    
    return result
    
    
    
    
        
        
    
    
        