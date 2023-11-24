import sys
from collections import deque

def bfs(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    sheep_cnt, wolf_cnt = 0, 0
    
    if yard[x][y] == "o":
        sheep_cnt += 1
    
    if yard[x][y] == "v":
        wolf_cnt += 1
    
    queue = deque()
    queue.append([x, y])
    visited[x][y] = True
    
    while queue:
        cur_x, cur_y = queue.popleft()
        
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            
            if 0 <= nx < r and 0 <= ny < c:  # Corrected the indices
                if not visited[nx][ny] and yard[nx][ny] != "#":  # Check if not visited and not a wall
                    visited[nx][ny] = True
                    queue.append([nx, ny])
                    
                    if yard[nx][ny] == "o":
                        sheep_cnt += 1
    
                    if yard[nx][ny] == "v":
                        wolf_cnt += 1
    
    return sheep_cnt, wolf_cnt
    
r, c = map(int, sys.stdin.readline().split())

yard = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(r)]

visited = [[False for _ in range(c)] for _ in range(r)]

living_sheep_cnt = 0
living_wolf_cnt = 0

for i in range(r):
    for j in range(c):  
        if yard[i][j] != "#" and not visited[i][j]:  
            sheep_cnt, wolf_cnt = bfs(i, j)  
            
            if sheep_cnt > wolf_cnt:
                wolf_cnt = 0
            else:
                sheep_cnt = 0
            
            living_sheep_cnt += sheep_cnt
            living_wolf_cnt += wolf_cnt

print("{} {}".format(living_sheep_cnt, living_wolf_cnt))