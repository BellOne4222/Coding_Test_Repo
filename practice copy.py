import sys
from collections import deque

def bfs(x,y,trashes):
    trash = 0
    
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    queue = deque()
    queue.append([x,y])
    visited[x][y] = True
    
    while queue:
        cur_x, cur_y = queue.popleft()
        trash += 1
        
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny]:
                    if graph[nx][ny] == 1:
                        visited[nx][ny] = True
                        queue.append([nx,ny])
    
    trashes.append(trash)
    
    return trashes
    
    
n,m,k = map(int, sys.stdin.readline().split())

graph = [[0 for _ in range(m)] for _ in range(n)] # [[1, 0, 0, 0], [0, 1, 1, 0], [1, 1, 0, 0]]

for _ in range(k):
    dump_x, dump_y = map(int, sys.stdin.readline().split())
    graph[dump_x-1][dump_y-1] = 1

visited = [[False for _ in range(m)] for _ in range(n)]

trashes = []

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            bfs(i,j,trashes)

print(max(trashes))



