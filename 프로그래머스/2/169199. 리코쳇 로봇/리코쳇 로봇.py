# 참고 : https://velog.io/@mimmimmu/PGS-%EB%A6%AC%EC%BD%94%EC%B3%87-%EB%A1%9C%EB%B4%87-%ED%8C%8C%EC%9D%B4%EC%8D%AC

from collections import deque

def solution(board):
    result = 0
    
    R = len(board)
    C = len(board[0])
    
    cur_x, cur_y = 0, 0
    
    # 로봇의 초기 위치 찾기
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
            
            # 목표지점에 도달하면 최단 거리 반환
            if board[cx][cy] == 'G':
                return visited[cx][cy]
            
            for i in range(4):
                nx, ny = cx, cy
                
                # 미끄러지는 동안의 이동 처리
                while True:
                    nx, ny = nx + dx[i], ny + dy[i]
                    
                    # 장애물에 부딪히거나, 맨 끝에 도달하면 멈춤
                    if 0 <= nx < R and 0 <= ny < C and board[nx][ny] == 'D':
                        nx -= dx[i]
                        ny -= dy[i]
                        break
                    
                    if nx < 0 or nx >= R or ny < 0 or ny >= C:
                        nx -= dx[i]
                        ny -= dy[i]
                        break
                    
                # 방문하지 않은 위치라면 큐에 추가하고 거리 갱신
                if not visited[nx][ny]:
                    visited[nx][ny] = visited[cx][cy] + 1
                    queue.append((nx, ny))
        
        # 목표지점에 도달할 수 없는 경우
        return -1
    
    # BFS를 통해 최소 이동 횟수 계산
    result = bfs()
    
    # 결과값이 양수일 경우, 시작 위치에서 목표 위치까지의 이동 횟수를 나타내므로 1을 빼줌
    if result > 0:
        result -= 1
        
    return result