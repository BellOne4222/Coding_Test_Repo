from collections import deque

def rotate_gears(wheels, wheel_num, direction):
    n = len(wheels)
    rotate = [0] * n  # 각 톱니바퀴의 회전 방향을 저장할 배열 (0: 회전 안함, 1: 시계 방향, -1: 반시계 방향)
    
    # 선택된 톱니바퀴를 회전시킬 방향을 설정
    rotate[wheel_num - 1] = direction

    # 선택된 톱니바퀴의 왼쪽 톱니바퀴들에 대한 회전 전파 검사
    for i in range(wheel_num - 1, 0, -1):
        if wheels[i][6] != wheels[i - 1][2]:
            rotate[i - 1] = -rotate[i]  # 맞닿은 극이 다르면 반대 방향으로 회전
        else:
            break  # 같은 극을 만나면 그 이후의 톱니바퀴는 영향을 받지 않으므로 중단

    # 선택된 톱니바퀴의 오른쪽 톱니바퀴들에 대한 회전 전파 검사
    for i in range(wheel_num - 1, n - 1):
        if wheels[i][2] != wheels[i + 1][6]:
            rotate[i + 1] = -rotate[i]  # 맞닿은 극이 다르면 반대 방향으로 회전
        else:
            break  # 같은 극을 만나면 그 이후의 톱니바퀴는 영향을 받지 않으므로 중단

    # 계산된 회전 방향에 따라 모든 톱니바퀴 회전 적용
    for i in range(n):
        wheels[i].rotate(rotate[i])

def calculate_score(wheels):
    points = [1, 2, 4, 8]  # 각 톱니바퀴의 점수 가중치
    score = 0
    for i in range(4):
        if wheels[i][0] == 1:  # 12시 방향의 극이 S극(1)이면 점수를 추가
            score += points[i]
    return score

# 톱니바퀴 상태 입력
wheels = []
for _ in range(4):
    wheel = deque(map(int, input().strip()))  # 입력받은 톱니바퀴 상태를 deque로 변환하여 회전을 용이하게 함
    wheels.append(wheel)

# 회전 횟수와 회전 명령 입력
k = int(input())
for _ in range(k):
    wheel_num, direction = map(int, input().split())  # 회전할 톱니바퀴 번호와 방향 입력
    rotate_gears(wheels, wheel_num, direction)  # 회전 함수 호출

# 결과 점수 계산 및 출력
print(calculate_score(wheels))  # 최종 점수 출력
