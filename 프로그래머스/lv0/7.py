# 각도기

def solution(angle):
    if angle > 0 and angle < 90:
        answer = 1
    elif angle == 90:
        answer = 2
    elif angle > 90 and angle < 180:
        answer = 3
    else :
        answer = 4
    return answer

print(solution(70))
print(solution(91))
print(solution(180))