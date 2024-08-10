import sys
from collections import deque

def bfs():
    queue = deque()
    max_distance = 0  # 안전 거리의 최댓값을 저장할 변수
    
    # 큐에 모든 아기 상어의 위치를 저장하고, 방문 처리
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                queue.append((i, j))
                visited[i][j] = True
    
    while queue:
        cur_x, cur_y = queue.popleft()
        
        dx = [-1,-1,0,1,1,1,0,-1]
        dy = [0,1,1,1,0,-1,-1,-1]
    
        for i in range(8):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
        
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    grid[nx][ny] = grid[cur_x][cur_y] + 1
                    max_distance = max(max_distance, grid[nx][ny])  # 최대값 갱신
                    queue.append([nx,ny])
    
    return max_distance - 1
                

n, m = map(int, sys.stdin.readline().split())

grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

visited = [[False for _ in range(m)] for _ in range(n)]

safe_distance = bfs()
print(safe_distance)