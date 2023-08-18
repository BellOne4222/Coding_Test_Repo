# 피자 나눠 먹기(3)

def solution(slice, n):
    answer = n // slice # 몫
    if (n % slice) >= 1: # 나머지
        answer += 1
        
    return answer