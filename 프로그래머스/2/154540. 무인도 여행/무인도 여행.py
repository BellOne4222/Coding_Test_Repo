from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(maps,x,y,visited):
    queue = deque()
    queue.append([x,y])
    visited[x][y] = True
    day = 0
    
    while queue:
        cur_x, cur_y = queue.popleft()
        day += int(maps[cur_x][cur_y])
        
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
                if maps[nx][ny] != "X" and not visited[nx][ny]:
                    queue.append([nx,ny])
                    visited[nx][ny] = True
    return day
    



def solution(maps):
    maps = list(map(list, maps)) # 	[['X', '5', '9', '1', 'X'], ['X', '1', 'X', '5', 'X'], ['X', '2', '3', '1', 'X'], ['1', 'X', 'X', 'X', '1']]
    visited = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
    
    result = []
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != "X" and not visited[i][j]:
                result.append(bfs(maps,i,j,visited))
    
    result.sort()
    if result:
        return result
    else:
        return [-1]
    
    
    