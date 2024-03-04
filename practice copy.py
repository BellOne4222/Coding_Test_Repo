import sys
from collections import deque
graph = [list(sys.stdin.readline().rstrip()) for _ in range(5)]
princess = 0

for i in range(5):
    for j in range(5):
        if graph[i][j] == "S":
            total_cnt = 1
            s_cnt = 1
            y_cnt = 0
            visited = [[False]*5 for _ in range(5)]
            queue = deque()
            queue.append([i,j])
            visited[i][j] = True
            
            dx = [-1,1,0,0]
            dy = [0,0,-1,1]
            
            while queue:
                cur_x, cur_y = queue.popleft()
                
                for k in range(4):
                    nx = cur_x + dx[k]
                    ny = cur_y + dy[k]
                    
                    if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:
                        if graph[nx][ny] == "Y":
                            y_cnt += 1
                        if graph[nx][ny] == "S":
                            s_cnt += 1
                        visited[nx][ny] = True
                        queue.append([nx,ny])
                        total_cnt += 1
                        
                        if y_cnt > 3:
                            break
                        if s_cnt >= 4 and total_cnt == 7:
                            princess += 1

print(princess)