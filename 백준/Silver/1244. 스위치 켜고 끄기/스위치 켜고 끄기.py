import sys

def turn_switch(idx):
    # 이 함수는 `idx` 인덱스에 해당하는 스위치의 상태를 토글합니다.
    # 스위치가 꺼져 있으면(0) 켜고(1), 켜져 있으면(0) 끕니다.
    if switches[idx] == 0:
        switches[idx] = 1
    elif switches[idx] == 1:
        switches[idx] = 0

# 입력으로부터 스위치의 총 개수를 읽습니다.
switch_num = int(sys.stdin.readline())

# 스위치 인덱스를 1부터 시작하게 하기 위해 맨 앞에 -1을 추가하여 스위치 리스트를 초기화합니다.
origin_switches = [-1]

# 스위치의 초기 상태를 읽고 `origin_switches` 리스트와 결합합니다.
switches = origin_switches + list(map(int, sys.stdin.readline().split()))

# 입력으로부터 학생의 수를 읽습니다.
student_num = int(sys.stdin.readline())

# 각 학생의 행동을 처리합니다.
for _ in range(student_num):
    male, given_num = map(int, sys.stdin.readline().split())
    
    # 학생이 남학생(1)이면, 주어진 수의 배수인 모든 스위치의 상태를 토글합니다.
    if male == 1:
        for i in range(1, switch_num//given_num + 1):
            turn_switch(i*given_num)
    
    # 학생이 여학생(2)이면, 주어진 스위치 번호를 중심으로 대칭이면서 가장 많은 스위치를 포함하는
    # 구간을 찾아 그 구간에 속한 모든 스위치의 상태를 토글합니다.
    elif male == 2:
        turn_switch(given_num)
        left_idx = given_num - 1
        right_idx = given_num + 1
        
        # 가능한 한 멀리 대칭 구간을 확장합니다. 좌우 인덱스에 있는 스위치의 상태가 같은 경우
        # 계속해서 대칭 구간을 넓혀 나갑니다.
        while True:
            if left_idx > 0 and right_idx <= switch_num and switches[left_idx] == switches[right_idx]:
                turn_switch(left_idx)
                turn_switch(right_idx)
            else:
                break
            left_idx -= 1
            right_idx += 1

# 최종 스위치의 상태를 출력합니다. 한 줄에 20개씩 출력하도록 지정되어 있습니다.
for j in range(1, switch_num+1):
    print(switches[j], end = " ")
    if j % 20 == 0 :
        print()