import sys  # sys 모듈을 불러옵니다.
from collections import deque


def bfs(x,y,visited):
    
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    queue = deque()
    queue.append([x,y])
    visited[x][y] = True
    trash = 0
    
    while queue:
        cur_x, cur_y = queue.popleft()
        trash += 1
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and path[nx][ny]:
                visited[nx][ny] = True
                queue.append([nx,ny])
    
    return trash
                

n,m,k = map(int, sys.stdin.readline().split())

path = [[0] * m for _ in range(n)]
visited = [[0] * m for _ in range(n)]
max_trash = 0

for _ in range(k):
    r,c = map(int, sys.stdin.readline().split())
    path[r-1][c-1] = 1
    
for i in range(n):
    for j in range(m):
        if not visited[i][j] and path[i][j]:
            answer = bfs(i,j,visited)
            max_trash = max(max_trash, answer)
                

print(max_trash)