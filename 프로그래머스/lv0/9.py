# 짝수의 합

def solution(n):
    answers = []
    for n in range(1,n+1):
        if n%2 == 0:
            answers.append(n)
    answer = sum(answers)
    return answer

print(solution(10))
print(solution(4))