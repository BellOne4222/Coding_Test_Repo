# 해당 x좌표에서 가질 수 있는 y좌표의 최소, 최대 정수 값을 구하기
# Math.floor() : 소수점 이하를 버림한다.
# Math.ceil() : 소수점 이하를 올림한다.
# Math.round() : 소수점 이하를 반올림한다.
# 제 풀이와 로직이나 아이디어는 똑같은데 코드가 다르고 새로운 내장함수를 사용해서 참고하였습니다.

import math

def solution(r1, r2):
    inner_dot_num = 0
    for x in range(1, r2 + 1):
        y_max = math.floor(math.sqrt(r2**2 - x**2))
        y_min = 0 if x >= r1 else math.ceil(math.sqrt(abs(r1**2 - x**2)))
        inner_dot_num += y_max - y_min + 1
    
    return inner_dot_num * 4
