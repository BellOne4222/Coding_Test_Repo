import sys
from collections import deque

# BFS 함수 정의
def bfs(x, y, graph):
    house = 1  # 단지 내 집의 수를 저장할 변수
    queue = deque()  # BFS를 위한 큐 생성
    queue.append([x, y])  # 시작점 추가
    visited[x][y] = True  # 시작점 방문 표시

    dx = [1, -1, 0, 0]  # 이동할 수 있는 방향 (상, 하, 좌, 우)
    dy = [0, 0, 1, -1]

    while queue:
        cur_x, cur_y = queue.popleft()  # 큐에서 현재 위치를 꺼내옴

        for i in range(4):  # 상하좌우 방향에 대해 탐색
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
                if not visited[nx][ny]:  # 방문하지 않은 집인 경우
                    queue.append([nx, ny])  # 다음 위치를 큐에 추가
                    visited[nx][ny] = True  # 해당 위치를 방문했다고 표시
                    house += 1  # 집의 수 증가
                    
    return house  # 현재 단지의 집 수 반환


n = int(sys.stdin.readline())  # 지도의 크기 입력

graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]  # 지도 정보 입력

visited = [[False for _ in range(n)] for _ in range(n)]  # 방문 여부를 저장할 2차원 리스트 초기화

houses = []  # 각 단지 내 집의 수를 저장할 리스트

# 모든 지점에 대해 탐색
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:  # 집이 있고 아직 방문하지 않은 곳인 경우
            houses.append(bfs(i, j, graph))  # BFS 탐색을 시작하고 집의 수를 리스트에 추가

houses.sort()  # 집의 수를 오름차순으로 정렬

print(len(houses))  # 총 단지 수 출력
for k in range(len(houses)):
    print(houses[k])  # 각 단지 내 집의 수 출력