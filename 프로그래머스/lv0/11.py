# 양꼬치

def solution(n, k):
    if n >= 10:
        answer = (12000 * n) + (2000 * (k-(int(n/10))))
    else :
        answer = (12000 * n) + (2000 * k)
    return answer

print(solution(10,3))
print(solution(64,6))