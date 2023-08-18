# 피자 나눠먹기(1)

def solution(n):
    answer = (n//7)
    answers = (n%7)
    if answer < 1:
        answer = 1
    elif answer >= 1 and answers != 0:
        answer += 1 
    return answer

print(solution(7))
print(solution(1))
print(solution(15))