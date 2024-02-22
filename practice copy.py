import sys
from collections import deque

def bfs():
    # BFS를 위한 큐 초기화
    queue = deque()
    queue.append([0,0])
    visited[0][0] = True
    hour_melting_cheese = 0
    
    # BFS 탐색
    while queue:
        cur_x, cur_y = queue.popleft()
        
        # 상하좌우 탐색
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            
            # 범위 내에 있고 방문하지 않은 칸이면
            if 0 <= nx < r and 0 <= ny < c:
                if not visited[nx][ny]:
                    if graph[nx][ny] == 0:
                        # 공기인 경우 방문 처리 후 큐에 추가
                        visited[nx][ny] = True
                        queue.append([nx,ny])
                    
                    elif graph[nx][ny] == 1:
                        # 치즈인 경우 녹이고 녹은 치즈 개수 증가
                        graph[nx][ny] = 0
                        visited[nx][ny] = True
                        hour_melting_cheese += 1
    
    # 녹은 치즈 개수를 리스트에 저장하고 반환
    cheeses.append(hour_melting_cheese)
    return hour_melting_cheese

# 입력 처리
r,c = map(int, sys.stdin.readline().split())

graph = []

for i in range(r):
    line = list(map(int, sys.stdin.readline().split()))
    graph.append(line)

# 남아있는 치즈 개수를 저장할 리스트
cheeses = []

time = 0

# 상하좌우 이동을 위한 dx, dy 리스트
dx = [1,-1,0,0]
dy = [0,0,1,-1]
 
while True:
    # 시간 증가
    time += 1
    visited = [[False for _ in range(c)] for _ in range(r)]
    melting_cheese = bfs()
    # 녹은 치즈가 없으면 종료
    if melting_cheese == 0:
        break

# 출력
print(time-1) # 시간 -1 반환
print(cheeses[-2]) # 다 녹기 한시간 전에 남은 치즈 개수