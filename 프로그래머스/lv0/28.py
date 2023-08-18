# 아이스 아메리카노

def solution(money):
    m1 = money // 5500
    m2 = money - (m1 * 5500)
    answer = [m1, m2]
    return answer
