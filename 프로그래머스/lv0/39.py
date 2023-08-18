# 제곱수 판별하기

import math #math 라이브러리 sqrt 사용하기 위해서 사용

def solution(n):
    a = int(math.sqrt(n))
    if a*a == n:
        answer = 1
    else:
        answer = 2
    return answer