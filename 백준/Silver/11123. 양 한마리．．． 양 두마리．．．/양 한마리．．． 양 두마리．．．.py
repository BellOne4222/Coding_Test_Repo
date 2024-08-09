import sys
sys.setrecursionlimit(100000)

def dfs(x,y):
    
    visited[x][y] = True
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < h and 0 <= ny < w:
            if grid[nx][ny] == "#" and not visited[nx][ny]:
                visited[nx][ny] = True
                dfs(nx,ny)
            
    

t = int(sys.stdin.readline())

for _ in range(t):
    h,w = map(int, sys.stdin.readline().split())
    
    grid = [list(sys.stdin.readline().rstrip()) for _ in range(h)]
    sheep_group = 0
    visited = [[False for _ in range(w)] for _ in range(h)]
    
    for i in range(h):
        for j in range(w):
            if grid[i][j] == "#" and not visited[i][j]:
                sheep_group += 1
                dfs(i,j)

    print(sheep_group)