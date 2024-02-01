from collections import deque

def solution(board):
    
    result = 0
    
    R = len(board)
    C = len(board[0])
    
    cur_x, cur_y = 0, 0
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "R":
                cur_x, cur_y = i, j
                
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    def bfs():
        queue = deque()
        queue.append((cur_x, cur_y))
        visited = [[0]*C for _ in range(R)]
        visited[cur_x][cur_y] = 1
        
        while queue:
            
            cx, cy = queue.popleft()
            
            if board[cx][cy] == 'G':
                return visited[cx][cy]
            
            for i in range(4):
                
                nx, ny = cx, cy
                
                while True:
                    nx, ny = nx+dx[i], ny+dy[i]
                    
                    if 0 <= nx < R and 0 <= ny < C and board[nx][ny]=='D':
                        nx -= dx[i]
                        ny -= dy[i]
                        break
                    
                    if nx < 0 or nx >= R or ny < 0 or ny >= C:
                        nx -= dx[i]
                        ny -= dy[i]
                        break
                    
                if not visited[nx][ny]:
                    visited[nx][ny] = visited[cx][cy] + 1
                    queue.append((nx, ny))
        return -1
                    
    result = bfs()
    
    if result > 0:
        result -= 1
        
    return result           