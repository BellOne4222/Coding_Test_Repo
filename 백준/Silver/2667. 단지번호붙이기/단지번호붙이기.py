import sys
from collections import deque

def bfs(x,y):
    link = 1
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
            
            if 0 <= nx < n and 0 <= ny < n:
                if grid[nx][ny] == 1 and not visited[nx][ny]:
                    link += 1
                    queue.append([nx,ny])
                    visited[nx][ny] = True
    return link                
        

n = int(sys.stdin.readline())

grid = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]

visited = [[False for _ in range(n)] for _ in range(n)]

houses = []

for i in range(n):
    for j in range(n):
        if grid[i][j] == 1 and not visited[i][j]:
            house = bfs(i,j)
            houses.append(house)

houses.sort()

print(len(houses))
for k in houses:
    print(k)
            