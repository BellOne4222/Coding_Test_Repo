from collections import deque
import sys

def bfs(x,y):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    sheep_cnt, wolf_cnt = 0,0
    
    if yard[x][y] == "o":
        sheep_cnt += 1
    
    if yard[x][y] == "v":
        wolf_cnt += 1
    
    queue = deque()
    queue.append([x,y])
    visited[x][y] = True
    
    while queue:
        cur_x, cur_y = queue.popleft()
        
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            
            if 0 <= nx < c and 0 <= ny < r:
                visited[nx][ny] = True
                queue.append([nx,ny])
                
                if yard[nx][ny] == "o":
                    sheep_cnt += 1
    
                if yard[nx][ny] == "v":
                    wolf_cnt += 1
    
    return sheep_cnt, wolf_cnt
    
r,c = map(int, sys.stdin.readline().split())

yard = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(r)] 
# [['.', '.', '.', '#', '.', '.', '\n'], ['.', '#', '#', 'v', '#', '.', '\n'], ['#', 'v', '.', '#', '.', '#', '\n'], ['#', '.', 'o', '#', '.', '#', '\n'], ['.', '#', '#', '#', '.', '#', '\n'], ['.', '.', '.', '#', '#', '#', '\n']]

visited = [[False for _ in range(r)] for _ in range(c)]

living_sheep_cnt = 0
living_wolf_cnt = 0

for i in range(c):
    for j in range(r):
        if yard[c][r] != "#" and not visited[c][r]:
            sheep_cnt, wolf_cnt = bfs(c,r)
            
            if sheep_cnt > wolf_cnt:
                wolf_cnt = 0
            else:
                sheep_cnt = 0
            
            living_sheep_cnt += sheep_cnt
            living_wolf_cnt += wolf_cnt

print("{} {}".format(living_sheep_cnt, living_wolf_cnt))