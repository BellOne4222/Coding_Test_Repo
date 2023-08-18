# 나이 출력

def solution(age):
    answer = 2022 - age + 1
    print("2022년 기준 {0}살 이므로, {1}년생입니다.".format(age, answer))
    return answer

print(solution(40))
print(solution(23))