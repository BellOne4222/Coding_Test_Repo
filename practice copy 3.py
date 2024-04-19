import sys
from collections import deque

def move_dice(dice, direction):
    new_dice = [0] * 6
    
    if direction == 0:  # 동쪽
        new_dice[0] = dice[3]
        new_dice[1] = dice[1]
        new_dice[2] = dice[0]
        new_dice[3] = dice[5]
        new_dice[4] = dice[4]
        new_dice[5] = dice[2]
        
    elif direction == 1:  # 서쪽
        new_dice[0] = dice[2]
        new_dice[1] = dice[1]
        new_dice[2] = dice[5]
        new_dice[3] = dice[0]
        new_dice[4] = dice[4]
        new_dice[5] = dice[3]
        
        
    elif direction == 2:  # 남쪽
        new_dice[0] = dice[1]
        new_dice[1] = dice[5]
        new_dice[2] = dice[2]
        new_dice[3] = dice[3]
        new_dice[4] = dice[0]
        new_dice[5] = dice[4]
        
    elif direction == 3:  # 북쪽
        new_dice[0] = dice[4]
        new_dice[1] = dice[0]
        new_dice[2] = dice[2]
        new_dice[3] = dice[3]
        new_dice[4] = dice[5]
        new_dice[5] = dice[1]
        
    return new_dice

n,m,k = map(int, sys.stdin.readline().strip().split())
graph = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)] 

total_score = 0

cur_dice = [1,2,3,4,5,6]
cur_x, cur_y = 0,0
cur_direction = 0 # 동쪽

move_cnt = 0

# 동서남북 이동
dx = [0,0,1,-1]
dy = [1,-1,0,0]

while move_cnt < k:
    
    # 1. 주사위가 이동 방향으로 한 칸 굴러간다.
    next_x, next_y = cur_x + dx[cur_direction], cur_y + dy[cur_direction]
       
    # 1-1. 만약, 이동 방향에 칸이 없다면, 이동 방향을 반대로 한 다음 한 칸 굴러간다.
    if next_x < 0 or next_y < 0 or next_x >= n or next_y >= m:
        if cur_direction == 0:
            cur_direction = 1
        elif cur_direction == 1:
            cur_direction = 0
        elif cur_direction == 2:
            cur_direction = 3
        else:
            cur_direction = 2
        continue
    
    move_cnt += 1
    
    new_dice = move_dice(cur_dice, cur_direction)
    
    queue = deque()
    visited = [[False for _ in range(m)] for _ in range(n)]
    queue.append([next_x, next_y])
    visited[next_x][next_y] = True
    c = 1
    
    while queue:
        cur_bfs_x, cur_bfs_y = queue.popleft()
        
        for i in range(4):
            nx = cur_bfs_x + dx[i]
            ny = cur_bfs_y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                b = graph[next_x][next_y]
                if not visited[nx][ny]:
                    if b == graph[nx][ny]:
                        queue.append([nx,ny])
                        visited[nx][ny] = True
                        c += 1
    
    total_score += (b * c)
    
    a = new_dice[5]
    b = graph[next_x][next_y]
    
    if a > b:
        if cur_direction == 0:
            cur_direction = 2
        elif cur_direction == 1:
            cur_direction = 3
        elif cur_direction == 2:
            cur_direction = 1
        elif cur_direction == 3:
            cur_direction = 0
    elif a < b:
        if cur_direction == 0:
            cur_direction = 3
        elif cur_direction == 1:
            cur_direction = 2
        elif cur_direction == 2:
            cur_direction = 0
        elif cur_direction == 3:
            cur_direction = 1
    
    cur_x, cur_y, cur_dice = next_x, next_y, new_dice

print(total_score)
        