import sys

def dfs(cur_x, cur_y, prev_x, prev_y, dot_cnt):
    if dot_cnt >= 4 and visited[cur_x][cur_y]:
        return True
    
    dx= [1, -1, 0, 0]
    dy= [0, 0, 1, -1]
    visited[cur_x][cur_y] = True
    for i in range(4):
        nx = cur_x + dx[i]
        ny = cur_y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == graph[cur_x][cur_y]:
                if [nx,ny] != [prev_x, prev_y]:
                    if dfs(nx,ny,cur_x,cur_y,dot_cnt+1):
                        return True
    visited[cur_x][cur_y] = False
    return False

n, m = map(int, sys.stdin.readline().split())
graph = [sys.stdin.readline().rstrip() for _ in range(n)]
visited = [[False]*m for _ in range(n)]
flag = False

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            if dfs(i,j,i,j,0):
                flag = True
                break
    if flag:
        break

if flag:
    print("Yes")
else:
    print("No")