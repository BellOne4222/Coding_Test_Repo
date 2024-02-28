import sys
from collections import deque

def bfs(x,y):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    queue = deque()
    queue.append((x,y))
    visited[x][y] = 0  # 시작 위치의 visited 값을 0으로 설정
    
    while queue:
        cur_x, cur_y = queue.popleft()
        
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 0 and visited[nx][ny] > visited[cur_x][cur_y]:
                    visited[nx][ny] = visited[cur_x][cur_y] + 1
                    queue.append((nx,ny))
                    
                elif graph[nx][ny] == 1 and visited[nx][ny] > visited[cur_x][cur_y]:
                    visited[nx][ny] = visited[cur_x][cur_y]
                    queue.append((nx,ny))

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
visited = [[1e9]*n for _ in range(n)]  # visited 리스트를 float('inf')로 초기화

bfs(0,0)

print(visited[n-1][n-1])