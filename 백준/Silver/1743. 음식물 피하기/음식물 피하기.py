import sys
from collections import deque

def bfs(x,y,trashes):
    trash = 0
    
    dx = [1,-1,0,0]  # 상하좌우 이동을 위한 x 좌표 변화량
    dy = [0,0,1,-1]  # 상하좌우 이동을 위한 y 좌표 변화량
    
    queue = deque()  # 너비 우선 탐색을 위한 큐 생성
    queue.append([x,y])  # 시작 지점 큐에 추가
    visited[x][y] = True  # 시작 지점 방문 처리
    
    while queue:  # 큐가 빌 때까지 반복
        cur_x, cur_y = queue.popleft()  # 큐에서 하나의 지점을 꺼내옴
        trash += 1  # 음식물 크기 증가
        
        for i in range(4):  # 상하좌우 이동을 위한 반복문
            nx = cur_x + dx[i]  # 새로운 x 좌표 계산
            ny = cur_y + dy[i]  # 새로운 y 좌표 계산
            
            if 0 <= nx < n and 0 <= ny < m:  # 그래프 범위 내에 있는지 확인
                if not visited[nx][ny]:  # 방문하지 않았던 곳인지 확인
                    if graph[nx][ny] == 1:  # 음식물이 있는 곳인지 확인
                        visited[nx][ny] = True  # 방문 처리
                        queue.append([nx,ny])  # 큐에 새로운 지점 추가
    
    trashes.append(trash)  # 현재 음식물 크기를 리스트에 추가
    
    return trashes  # 음식물 크기 리스트 반환
    
    
n,m,k = map(int, sys.stdin.readline().split())  # 행, 열, 음식물 개수 입력 받기

graph = [[0 for _ in range(m)] for _ in range(n)]  # 그래프 초기화

for _ in range(k):  # 음식물 좌표 입력 받기
    dump_x, dump_y = map(int, sys.stdin.readline().split())
    graph[dump_x-1][dump_y-1] = 1  # 음식물이 있는 좌표 1로 표시

visited = [[False for _ in range(m)] for _ in range(n)]  # 방문 여부를 나타내는 배열 초기화

trashes = []  # 음식물 크기를 담을 리스트

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:  # 음식물이 있고 방문하지 않았다면
            bfs(i,j,trashes)  # bfs 탐색 실행

print(max(trashes))  # 가장 큰 음식물 크기 출력