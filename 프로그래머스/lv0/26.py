# 삼각형의 완성 조건(1)

def solution(sides):
    sides.sort()
    if (sides[0] + sides[1]) > sides[2]:
        answer = 1
    else:
        answer = 2
    return answer