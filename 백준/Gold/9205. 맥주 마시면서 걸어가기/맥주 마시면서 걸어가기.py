# 필요한 라이브러리를 불러옵니다.
import sys
from collections import deque

# 더 빠른 입력 처리를 위해 input 함수를 재정의합니다.
input = sys.stdin.readline

# 두 지점 사이의 맨해튼 거리를 계산하는 함수입니다.
def cal_distance(x, y, nx, ny):
    return abs(nx - x) + abs(ny - y)

# BFS를 사용하여 페스티벌에 도달할 수 있는지 검사하는 함수입니다.
def bfs():
    # 집에서 페스티벌까지의 거리가 1000미터 이내이면 도달 가능하다고 표시하고 함수를 종료합니다.
    if cal_distance(home_x, home_y, rock_x, rock_y) <= 1000:
        visited[n] = True
        return

    # BFS를 위한 큐를 초기화합니다.
    que = deque()

    # 집에서 1000미터 이내에 있는 편의점을 모두 큐에 추가하고 방문했다고 표시합니다.
    for i in range(len(conveni)):
        temp = cal_distance(home_x, home_y, conveni[i][0], conveni[i][1])
        if temp <= 1000:
            que.append(conveni[i])
            visited[i] = True

    # 큐에서 위치를 하나씩 꺼내며 편의점을 방문합니다.
    while que:
        # 현재 위치를 큐에서 꺼냅니다.
        cx, cy = que.popleft()
        # 모든 편의점에 대해 현재 위치에서 도달할 수 있는지 검사합니다.
        for i in range(len(conveni)):
            temp = cal_distance(cx, cy, conveni[i][0], conveni[i][1])
            # 1000미터 이내이고 아직 방문하지 않았다면 큐에 추가하고 방문했다고 표시합니다.
            if temp <= 1000 and not visited[i]:
                que.append(conveni[i])
                visited[i] = True

# 테스트 케이스의 수를 입력받습니다.
t = int(input())

for _ in range(t):
    # 편의점의 수를 입력받습니다.
    n = int(input())
    # 방문 여부를 확인하기 위한 리스트를 초기화합니다.
    visited = [False] * (n + 1)
    # 편의점 위치를 저장할 리스트를 초기화합니다.
    conveni = []

    # 집의 좌표를 입력받습니다.
    home_x, home_y = map(int, input().split())

    # 편의점의 위치를 입력받아 저장합니다.
    for _ in range(n):
        conveni.append([int(a) for a in input().split()])

    # 페스티벌의 위치를 입력받고 편의점 리스트에 추가합니다.
    rock_x, rock_y = map(int, input().split())
    conveni.append([rock_x, rock_y])

    # BFS를 실행하여 페스티벌에 도달할 수 있는지 검사합니다.
    bfs()

    # 결과에 따라 'happy' 또는 'sad'를 출력합니다.
    if visited[n] == True:
        print('happy')
    else:
        print('sad')
