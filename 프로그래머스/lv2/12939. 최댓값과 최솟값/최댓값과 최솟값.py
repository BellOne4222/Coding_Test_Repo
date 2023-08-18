def solution(s):
    lst = list(map(int, s.split())) # int로 형변환하여 리스트 생성
    lst.sort()
    
    result = "{} {}".format(min(lst), max(lst)) # 최댓값, 최솟값 반환
    return result
        
        
                   
        