import sys
from collections import deque

def bfs(x,y):
    global moving
    
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    
    move_lst = []
    
    queue = deque()
    queue.append([x,y])
    move_lst.append(board[x][y])
    visited[x][y] = True
    
    while queue:
        cur_x, cur_y = queue.popleft()
        
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if board[nx][ny] not in move_lst:       
                    if not visited[nx][ny]:
                        move_lst.append(board[nx][ny])
                        visited[nx][ny] = True
                        queue.append([nx,ny]) 
    
    moving = max(moving, len(move_lst))
        
        


r,c = map(int, sys.stdin.readline().split())

board = []

for _ in range(r):
    line = list(sys.stdin.readline().rstrip())
    board.append(line)
    

visited = [[False for _ in range(c)] for _ in range(r)]

moving = -1

bfs(0,0)

print(moving)
