import sys
sys.setrecursionlimit(5000)

def dfs(x, y):
    distance = 0
    visited[x][y] = True
    
    dx = [-1,-1,0,1,1,1,0,-1]
    dy = [0,1,1,1,0,-1,-1,-1]
    
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < m:
            if grid[nx][ny] == 0 and not visited[nx][ny]:
                distance += 1
                visited[nx][ny] = True
                dfs(nx,ny)
            elif grid[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                return distance
    
    return distance  # distance를 반환

n, m = map(int, sys.stdin.readline().split())

grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

safe_distance = 0

visited = [[False for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if grid[i][j] == 0 and not visited[i][j]:
            cnt = dfs(i, j)
            safe_distance = max(safe_distance, cnt)

print(safe_distance)
