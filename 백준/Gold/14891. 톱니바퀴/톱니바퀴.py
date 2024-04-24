from collections import deque

def rotate_gears(wheels, wheel_num, direction):
    n = len(wheels)
    rotate = [0] * n  # 각 톱니바퀴의 회전 방향을 저장할 배열 (0: 회전 안함, 1: 시계 방향, -1: 반시계 방향)
    rotate[wheel_num - 1] = direction

    # 왼쪽 톱니바퀴들에 대한 회전 전파
    for i in range(wheel_num - 1, 0, -1):
        if wheels[i][6] != wheels[i - 1][2]:
            rotate[i - 1] = -rotate[i]
        else:
            break

    # 오른쪽 톱니바퀴들에 대한 회전 전파
    for i in range(wheel_num - 1, n - 1):
        if wheels[i][2] != wheels[i + 1][6]:
            rotate[i + 1] = -rotate[i]
        else:
            break

    # 모든 계산된 회전 적용
    for i in range(n):
        wheels[i].rotate(rotate[i])

def calculate_score(wheels):
    points = [1, 2, 4, 8]
    score = 0
    for i in range(4):
        if wheels[i][0] == 1:  # S극이면
            score += points[i]
    return score

# 톱니바퀴 상태 입력
wheels = []
for _ in range(4):
    wheel = deque(map(int, input().strip()))
    wheels.append(wheel)

# 회전 횟수와 회전 명령 입력
k = int(input())
for _ in range(k):
    wheel_num, direction = map(int, input().split())
    rotate_gears(wheels, wheel_num, direction)

# 결과 점수 계산 및 출력
print(calculate_score(wheels))