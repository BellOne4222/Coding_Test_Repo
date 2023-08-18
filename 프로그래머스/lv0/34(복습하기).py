# 모음 제거

def solution(my_string):
    mo = ("a,e,i,o,u") # 모음을 모아준다
    answer = '' # 빈 문자열을 생성
    for i in my_string:
        if i not in mo: #not in을 사용하여 mo안에 없으면
            answer += i # 빈 문자열인 answer에 추가시켜 문자열 생성
    return answer
        