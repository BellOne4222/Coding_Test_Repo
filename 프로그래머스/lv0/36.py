# 자릿수 더하기

def solution(n):
    n = str(n)
    n = list(n) # 리스트로 변환 하기 위해 정수에서 문자열로 먼저 변경 후 리스트로 변경
    answers = (int(i) for i in n) # i를 정수형으로 변경
    answer = sum(answers) # 리스트 요소 합계
    return answer