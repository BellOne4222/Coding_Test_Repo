# bfs
from collections import deque
n,m = map(int,input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))
    
def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    # 상하좌우
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    while queue:
        x, y = queue.popleft()
        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]
            # 범위 내인지 확인
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽이므로 진행 불가
            if graph[nx][ny] == 0:
                continue
            # 갈 수 있는 칸이면,
            if graph[nx][ny] == 1:
                # 탐색 실행
                queue.append((nx,ny))
                # 다음 칸을 현재 칸에 +1을 해서 거리 표시
                graph[nx][ny] = graph[x][y] + 1
    return graph[n-1][m-1]

print(bfs(0,0))



