# 3. 그래서 반복을 3번으로 늘리면 2번째 시도의 문제점을 잡을 수 있을 것 같아서 3번으로 늘렸더니 테스트 케이스 11번 빼고 성공
# 그래서 질문하기에서 반례 탐색
# 반례 : [0,0,0,0] 일 때, 0으로 나와야 하는데 0000으로 결과가 반환 되기 때문에 실패


def solution(numbers):
    numbers_str = list(map(str, numbers))
    numbers_str.sort(key = lambda x : x*3, reverse = True)
    
    result = ''
    
    for l in range(len(numbers)):
        result += numbers_str[l]
    
    
    return result
    
    
    
    
        
        
    
    
        