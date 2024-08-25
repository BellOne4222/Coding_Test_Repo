import sys

c,r = map(int, sys.stdin.readline().split())

k = int(sys.stdin.readline())

grid = [[0 for _ in range(r)] for _ in range(c)]

visited = [[0 for _ in range(r)] for _ in range(c)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

cur = 1
cur_r = 0
cur_c = 0
dir = 0

for i in range(1, r*c+1):
    
    if i == k:
        break
    
    else:
        if 0 <= cur_c < c and 0 <= cur_r < r and not visited[cur_c][cur_r]:
            grid[cur_c][cur_r] = i
            visited[cur_c][cur_r] = True
            cur_c += dx[dir]
            cur_r += dy[dir]
        else:
            cur_c -= dx[dir]
            cur_r -= dy[dir]
            
            dir = (dir + 1) % 4

            cur_c += dx[dir]
            cur_r += dy[dir]
            
    
    
            
        
    