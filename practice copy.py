import sys
from collections import deque

dx = [-1, -1, -1, 0, 1, 0, 1, 1]
dy = [-1, 0, 1, 1, 1, -1, 0, -1]

# 입력 받기
n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 상어 위치 찾기
queue = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:  
            queue.append([i, j])

result = 0
# BFS를 통해 안전 거리 구하기 
while queue:
    x, y = queue.popleft()
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if graph[nx][ny] != 0:
            continue
        queue.append([nx, ny])
        graph[nx][ny] = graph[x][y] + 1
        result = max(result, graph[x][y] + 1)

# 안전 거리의 최댓값 출력하기 (시작 위치를 포함한 거리를 출력)
print(result - 1) # 상어의 위치를 제외하고 결과 출력