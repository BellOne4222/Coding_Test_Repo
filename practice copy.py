import sys
from collections import deque

def bfs(x, y, arr, visited):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    color = arr[x][y]
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    
    while queue:
        cur_x, cur_y = queue.popleft()
        
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] == color and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

N = int(sys.stdin.readline())
normal = [list(sys.stdin.readline().strip()) for _ in range(N)]
color_weakness = [[y if y != 'G' else 'R' for y in x] for x in normal]

normal_visited = [[False]*N for _ in range(N)]
color_weakness_visited = [[False]*N for _ in range(N)]

normal_cnt = color_weakness_cnt = 0

for i in range(N):
    for j in range(N):
        if not normal_visited[i][j]:
            bfs(i, j, normal, normal_visited)
            normal_cnt += 1
        if not color_weakness_visited[i][j]:
            bfs(i, j, color_weakness, color_weakness_visited)
            color_weakness_cnt += 1

print(normal_cnt, color_weakness_cnt)




