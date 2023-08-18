# 문자열 안에 문자열

def solution(str1, str2):
    if str2 in str1 : # 부분 문자열 확인은 in과 not in을 통해 확인 가능
        answer = 1
    else:
        answer = 2
    return answer