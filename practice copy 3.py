import sys
from collections import deque

def bfs(x,y):
    queue = deque()
    bfs_visited = [[0]*5 for _ in range(5)]
    queue.append([x,y])
    bfs_visited[x][y] = 1
    cnt = 1
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    while queue:
        cur_x, cur_y = queue.popleft()
        
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            
            if 0 <= nx < 5 and 0 <= ny < 5:
                if bfs_visited[nx][ny] == 0:
                    if visited[nx][ny] == 1:
                        queue.append([nx,ny])
                        bfs_visited[nx][ny] = 1
                        cnt += 1
    
    return cnt == 7
                        
                     

def check():
    for i in range(5):
        for j in range(5):
            if visited[i][j] == 1:
                return bfs(i,j)

def dfs(cnt, w_cnt, s_cnt):
    global princess
    if w_cnt > 7: # 가지치기(학생 수가 7명이상이면 종료)
        return
    
    if cnt == 25:
        if w_cnt == 7 and s_cnt >= 4: # 그룹 인원이 7명이고 s의 수가 4이상 일때
            if check(): # 인접했는지 체크해서 true 이면 princess += 1
                princess += 1
        
        return

    visited[cnt//5][cnt%5] = 1 # 포함하는 경우
    dfs(cnt+1, w_cnt+1, s_cnt + int(graph[cnt//5][cnt%5] == 'S'))
    visited[cnt//5][cnt%5] = 0 # 원상복구(백트래킹)
    dfs(cnt+1, w_cnt, s_cnt) # 포함하지 않는 경우
    
    

graph = [list(sys.stdin.readline().rstrip()) for _ in range(5)]
princess = 0
visited = [[0]*5 for _ in range(5)]
dfs(0,0,0)
print(princess)