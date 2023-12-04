import sys
from collections import deque

def bfs(i, j, puyo_color):
    
    global exploding_check
    
    same_color = 1
    
    explode_locations = []
    
    dr = [1,-1,0,0]
    dc = [0,0,1,-1]
    
    
    queue = deque()
    queue.append([i,j])
    explode_locations.append([i,j])
    visited[i][j] = True
    
    while queue:
        cur_r, cur_c = queue.popleft()
        for i in range(4):
            nr = cur_r + dr[i]
            nc = cur_c + dc[i]
            if 0 <= nr < 12 and 0 <= nc < 6:
                if field[nr][nc] == puyo_color:
                    if not visited[nr][nc]:
                        visited[nr][nc] = True
                        queue.append([nr,nc])
                        explode_locations.append([nr,nc])
                        same_color += 1
    
    if same_color >= 4:
        for location in explode_locations:
            field[location[0]][location[1]] = "."
            
        exploding_check = True


r = 12
c = 6

field = []

for i in range(r):
    line = list(sys.stdin.readline().rstrip())
    field.append(line)

colors = ["R", "G", "B", "P", "Y"]

chain = 0

while True:
    exploding_check = False
    
    visited = [[False for _ in range(c)] for _ in range(r)]
    
    for x in range(r):
        for y in range(c):
            if field[x][y] != ".":
                color = field[x][y]
                bfs(x,y,color)
    
    for i in range(6):
        rotate_queue = deque()

        for j in range(11,-1,-1):
            if field[j][i] != '.':
                rotate_queue.append(field[j][i])

        for j in range(11,-1,-1):
            if rotate_queue:
                field[j][i] = rotate_queue.popleft()
            else:
                field[j][i] = '.'
        
        
    
    if not exploding_check:
        break
    else:
        chain += 1

print(chain)