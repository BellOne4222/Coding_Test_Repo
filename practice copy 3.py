import sys
from collections import deque

def bfs(x, y, end_x, end_y, move, l):
    
    if x == end_x and y == end_y:
        return 0
    # 나이트가 이동 할 수 있는 8가지 방향
    dx = [-1,1,2,2,-2,-2,2,2]
    dy = [2,2,1,-1,1,-1,-1,1]
    
    queue = deque()
    queue.append((x, y, move))
    
    while queue:
        cur_x, cur_y, cur_move = queue.popleft()
        visited[cur_x][cur_y] = True
        
        for i in range(8):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            
            if 0 <= nx < l and 0 <= ny < l:
                if visited[nx][ny] == False:
                    visited[nx][ny] = True
                    queue.append((nx, ny, cur_move + 1))
                if nx == end_x and ny == end_y:
                    return cur_move + 1
        
    

t = int(sys.stdin.readline()) # 테스트 케이스의 개수


for i in range(t):
    l = int(sys.stdin.readline()) # 체스판의 한변의 길이
    start_x, start_y = map(int, sys.stdin.readline().split()) # 나이트의 현재 x,y좌표
    end_x, end_y = map(int, sys.stdin.readline().split())  # 나이트의 목적 x,y좌표
    
    visited = [[False] * l for _ in range(l)] # 방문 여부를 저장할 배열 초기화
    
    print(bfs(start_x, start_y, end_x, end_y, 0, l)) # 최소 이동 횟수 출력
