# 배열의 유사도

def solution(s1, s2):
    answers = list(set(s1).intersection(s2)) # 배열을 set으로 바꾸고 intersection을 통해 교집합을 도출
    answer = len(answers)
    return answer