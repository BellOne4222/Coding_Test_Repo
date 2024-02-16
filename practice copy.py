import sys
from collections import deque

def bfs(x,y,graph):
    house = 1
    queue = deque()
    queue.append([x,y])
    visited[x][y] = True
    
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    while queue:
        cur_x, cur_y = queue.popleft()
        
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
                if not visited[nx][ny]:
                    graph[nx][ny] = 0
                    queue.append([nx,ny])
                    visited[nx][ny] = True
                    house += 1
                    
    return house
                    
        
    
    

n = int(sys.stdin.readline())

graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
# [[0, 1, 1, 0, 1, 0, 0], [0, 1, 1, 0, 1, 0, 1], [1, 1, 1, 0, 1, 0, 1], [0, 0, 0, 0, 1, 1, 1], [0, 1, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 0], [0, 1, 1, 1, 0, 0, 0]]

visited = [[False for _ in range(n)] for _ in range(n)]

houses = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            houses.append(bfs(i,j,graph))

houses.sort()

print(len(houses))
for k in range(len(houses)):
    print(houses[k])
