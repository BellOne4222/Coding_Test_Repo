import sys

def dfs(cur_x, cur_y, prev_x, prev_y, dot_cnt):
    # 사이클이 형성된 경우
    if dot_cnt >= 4 and visited[cur_x][cur_y]:
        return True
    
    # 상하좌우 이동을 위한 리스트
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    # 현재 위치 방문 표시
    visited[cur_x][cur_y] = True
    
    # 상하좌우 이동 탐색
    for i in range(4):
        nx = cur_x + dx[i]
        ny = cur_y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            # 색이 같고 이전 위치와 다른 경우에만 탐색 진행
            if graph[nx][ny] == graph[cur_x][cur_y] and [nx, ny] != [prev_x, prev_y]:
                if dfs(nx, ny, cur_x, cur_y, dot_cnt + 1):
                    return True
    
    # 현재 위치 방문 표시 취소 (백트래킹)
    visited[cur_x][cur_y] = False
    return False

n, m = map(int, sys.stdin.readline().split())
graph = [sys.stdin.readline().rstrip() for _ in range(n)]
visited = [[False]*m for _ in range(n)]
flag = False

# 모든 점에 대해 DFS 탐색 진행
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            if dfs(i, j, i, j, 0):
                flag = True
                break
    if flag:
        break

if flag:
    print("Yes")
else:
    print("No")