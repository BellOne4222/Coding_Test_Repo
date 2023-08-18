# 숨어있는 숫자의 덧셈(1)

import re 

def solution(my_string):
    answer = re.findall(r'\d',my_string) #re 모듈의 findall 함수로 r'\d'라는 숫자들만 찾아서 리스트로 리턴한다.
    answer = [int(i) for i in answer] # 리스트 안에 있는 요소들을 정수 변환
    return sum(answer)

# https://codechacha.com/ko/python-extract-integers-from-string/