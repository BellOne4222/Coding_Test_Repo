# 2. 자릿수 채우는 방식을 0이 아닌 해당 원소를 2번 반복하는 방식으로 비교, 어차피 2번 반복을 해서 기존의 최대 숫자인 1000을 넘어도 문자열로 정렬을 할때는 맨 앞자리를 먼저 보고, 그 다음 뒷자리를 본다.
# 앞 두자리만 비교를 하기 때문에 구현했지만, 밑의 반례를 해결하지 못해 실패, 89와 898은 반복하고 앞 두자리 비교해도 89이기 때문에 해결 실패
# 질문하기에서 [1, 10, 100, 1000, 818, 81, 898, 89, 0, 0] => 89/898/818/81/1/10/100/1000/0/0 => "8989881881110100100000" 반례 참고


def solution(numbers):
    numbers_str = list(map(str, numbers))
    numbers_str.sort(key = lambda x : x*2, reverse = True) # 원소를 두번 반복해서 비교
    
    result = ''
    
    for l in range(len(numbers)):
        result += numbers_str[l]
    
    
    return result
    
    
    
    
        
        
    
    
        