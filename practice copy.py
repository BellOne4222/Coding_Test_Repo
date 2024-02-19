import sys
from collections import deque

def bfs(x, y, z):
    
    dx = [0, 0, 0, 0, 1, -1]
    dy = [0, 0, 1, -1, 0, 0]
    dz = [1, -1, 0, 0, 0, 0]
    
    queue = deque()
    queue.append((x, y, z, 0))
    
    while queue:
        cur_x, cur_y, cur_z, cur_time = queue.popleft()
        
        for i in range(6):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            nz = cur_z + dz[i]
            
            if 0 <= nx < l and 0 <= ny < r and 0 <= nz < c:
                if visited[nx][ny][nz] == False and buildings[nx][ny][nz] == '.':
                    visited[nx][ny][nz] = True
                    queue.append((nx, ny, nz, cur_time + 1))
                elif buildings[nx][ny][nz] == 'E' and visited[nx][ny][nz] == False:
                    return 'Escaped in ' + str(cur_time + 1) + ' minute(s).'
    
    return 'Trapped!'
                
        

while True:
    l, r, c = map(int, sys.stdin.readline().split())
    if l == 0 and r == 0 and c == 0:
        break
    
    buildings = []
    for i in range(l):
        buildings.append([list(sys.stdin.readline().strip()) for _ in range(r)])
        sys.stdin.readline()
        
    
    visited = [[[False] * c for _ in range(r)] for _ in range(l)]
    
    for j in range(l):
        for k in range(r):
            for m in range(c):
                if buildings[j][k][m] == 'S':
                    visited[j][k][m] = True
                    print(bfs(j, k, m))
                    break    
    
    
    