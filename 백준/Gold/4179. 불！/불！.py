import sys
from collections import deque

# 표준 입력으로 R과 C를 입력 받음
r, c = map(int, sys.stdin.readline().split())

# 미로 정보를 저장할 리스트를 초기화함
graph = [list(sys.stdin.readline().rstrip()) for _ in range(r)]

# 각각의 위치를 방문했는지 여부를 저장할 리스트를 초기화함
graph_visited = [[0]*c for _ in range(r)]
fire_visited = [[0]*c for _ in range(r)]

# 지훈이와 불의 위치를 저장할 큐를 초기화함
fire_queue = deque()
graph_queue = deque()

# 초기 위치 설정
for i in range(r):
    for j in range(len(graph[0])):
        if graph[i][j] == "J":
            graph_queue.append([i,j])
            graph_visited[i][j] = 1
        if graph[i][j] == "F":
            fire_queue.append([i,j])
            fire_visited[i][j] = 1
        
        if graph_visited[i][j] == 1 and fire_visited[i][j] == 1:
            break

# 상하좌우 이동을 위한 리스트
dx = [1,-1,0,0]
dy = [0,0,1,-1]

# BFS 알고리즘을 통해 불과 지훈이의 이동 경로를 계산하는 함수
def bfs():
    
    # 불의 이동 경로 계산
    while fire_queue:
        cur_x, cur_y = fire_queue.popleft()
        
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            
            if 0 <= nx < r and 0 <= ny < c: 
                if not fire_visited[nx][ny] and graph[nx][ny] != "#":
                    fire_visited[nx][ny] = fire_visited[cur_x][cur_y] + 1
                    fire_queue.append([nx,ny])
    
    # 지훈이의 이동 경로 계산        
    while graph_queue:
        cur_x, cur_y = graph_queue.popleft()
        
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            
            if 0 <= nx < r and 0 <= ny < c: 
                if not graph_visited[nx][ny] and graph[nx][ny] != "#":
                    # 불이 도달하지 않은 위치이거나, 현재 위치까지의 시간보다 더 빠른 경우에만 지훈이가 이동 가능함
                    if not fire_visited[nx][ny] or fire_visited[nx][ny] > graph_visited[cur_x][cur_y] + 1:
                        graph_visited[nx][ny] = graph_visited[cur_x][cur_y] + 1
                        graph_queue.append([nx,ny])
            
            else:
                return graph_visited[cur_x][cur_y]
    
    # 탈출 불가능한 경우 "IMPOSSIBLE" 반환
    return "IMPOSSIBLE"

# 결과 출력
print(bfs())