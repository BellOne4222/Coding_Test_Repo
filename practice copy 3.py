import sys
from collections import deque

def bfs(x, y, end_x, end_y):
    
    # 나이트가 이동 할 수 있는 8가지 방향
    dx = [-1,1,2,2,1,-1,-2,-2]
    dy = [2,2,1,-1,-2,-2,-1,1]
    
    queue = deque()
    queue.append((x, y))

    while queue:
        cur_x, cur_y = queue.popleft()
        
        if cur_x == end_x and cur_y == end_y:
            return visited[cur_x][cur_y] - 1
        
        for i in range(8):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            
            if 0 <= nx < l and 0 <= ny < l:
                if visited[nx][ny] == 0:
                    queue.append((nx, ny))
                    visited[nx][ny] = visited[cur_x][cur_y] + 1
                    
                
        
    

t = int(sys.stdin.readline()) # 테스트 케이스의 개수


for i in range(t):
    l = int(sys.stdin.readline()) # 체스판의 한변의 길이
    start_x, start_y = map(int, sys.stdin.readline().split()) # 나이트의 현재 x,y좌표
    end_x, end_y = map(int, sys.stdin.readline().split())  # 나이트의 목적 x,y좌표
    
    visited = [[0] * l for _ in range(l)] # 방문 여부를 저장할 배열 초기화
    visited[start_x][start_y] = 1
    
    print(bfs(start_x, start_y, end_x, end_y)) # 최소 이동 횟수 출력
