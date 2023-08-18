#  숫자 비교하기

def solution(num1, num2):
    if num1 == num2:
        answer = 1
    else :
        answer = -1
    return answer

print(solution(2,3))
print(solution(11,11))
print(solution(7,99))