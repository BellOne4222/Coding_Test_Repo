# 머쓱이보다 키 큰 사람

def solution(array, height):
    answer = 0
    for taller in array:
        if taller > height:
            answer += 1
    return answer