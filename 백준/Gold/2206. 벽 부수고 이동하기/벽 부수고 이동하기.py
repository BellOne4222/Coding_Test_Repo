import sys
from collections import deque

def bfs(x,y):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    queue = deque()
    queue.append([x,y,0]) # 부순 횟수도 추가
    path[x][y][0] = 1
    
    while queue:
        cur_x, cur_y, break_cnt = queue.popleft()
        
        if (cur_x,cur_y) == (n-1, m-1):
            return path[cur_x][cur_y][break_cnt]
        
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                
                if graph[nx][ny] == 1 and break_cnt == 0:
                    path[nx][ny][1] = path[cur_x][cur_y][0] + 1
                    queue.append([nx,ny,1])
                
                if graph[nx][ny] == 0 and path[nx][ny][break_cnt] == 0:
                    path[nx][ny][break_cnt] = path[cur_x][cur_y][break_cnt] + 1
                    queue.append([nx,ny,break_cnt])
    
    return -1

n,m = map(int, sys.stdin.readline().split())

graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]

path = [[[0,0] for _ in range(m)] for _ in range(n)]
# [[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]]


print(bfs(0,0))