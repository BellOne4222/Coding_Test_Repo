from collections import deque

def solution(numbers):
    numbers_str = list(map(str, numbers))
    
    nums_dict = {i:0 for i in numbers_str}
    
    change_lst = [] 
    for k in range(len(numbers)):
        change_lst.append([numbers_str[k].ljust(4,'0'),numbers_str[k]]) 
    
    change_lst.sort(key = lambda x:x[0], reverse = True)
    # [['6000', '6'], ['2000', '2'], ['1000', '10']]
    # [['9000', '9'], ['5000', '5'], ['3400', '34'], ['3000', '3'], ['3000', '30']]
    
    result = ''
    
    for l in range(len(numbers)):
        result += change_lst[l][1]
    
    return result