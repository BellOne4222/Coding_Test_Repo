from collections import deque
                    
def solution(board):
    
    # 상하좌우로 움직임은 가능하나 D가 나오거나, 보드판 끝까지로만 이동가능
    
    visited = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
    
    board = list(map(list,board)) # [['.', '.', '.', 'D', '.', '.', 'R'], ['.', 'D', '.', 'G', '.', '.', '.'], ['.', '.', '.', '.', 'D', '.', 'D'], ['D', '.', '.', '.', '.', 'D', '.'], ['.', '.', 'D', '.', '.', '.', '.']]
    
    def bfs(x,y,visited, board):
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]

        queue = deque()
        queue.append([x,y])
        visited[x][y] = 1

        while queue:
            cur_x, cur_y = queue.popleft()
            if board[cur_x][cur_y] == "G":
                return visited[cur_x][cur_y]

            for i in range(4):
                nx = x
                ny = y

                # 이동가능한 좌표 찾기
                while True:
                    nx, ny = nx+dx[i], ny+dy[i]

                    # 보드 범위 이내이면서 장애물을 만났을 경우
                    if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and board[nx][ny]=='D':
                        nx -= dx[i]
                        ny -= dy[i]
                        break

                    # 보드 범위 밖 즉 장애물을 만나지 않고 끝까지 미끄러질 경우
                    if nx < 0 or nx >= len(board) or ny < 0 or ny >= len(board[0]):
                        nx -= dx[i]
                        ny -= dy[i]
                        break

                    if visited[nx][ny] == 0:
                        visited[nx][ny] = visited[cur_x][cur_y] + 1
                        queue.append([nx,ny])

        return -1
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "R":
                result = bfs()
    
    if result > 0:
        result -= 1
        
    return result 