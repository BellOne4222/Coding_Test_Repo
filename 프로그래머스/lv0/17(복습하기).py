# 특정 문자 제거하기 (중복 제거도 신경써야함)

def solution(my_string, letter): # 문자열도 리스트랑 똑같다.
    answer = '' # 빈 문자열
    for i in my_string: # my_string 문자열을 하나하나 보면서 
        if i != letter: # letter과 같지 않은 문자는 빈 문자열인 answer에 넣는다.
            answer += i
    return answer


# 해설 : https://www.youtube.com/watch?v=oDzdfbIubys