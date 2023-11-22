from collections import deque
import sys
input = sys.stdin.readline

# 입력
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))


# bfs
direction = [(1,0), (0,1), (-1,0), (0,-1)]

def bfs(x, y):
    graph[x][y] = 0
    queue = deque([(x, y)]) # 시작지점
    size = 1 # 집 크기
    while queue:
        x, y = queue.popleft()
        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            # 범위 내 방문하지 않은 곳이면 탐색
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                size += 1
                queue.append((nx, ny))
    return size

cnt = 0
max_size = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            cnt += 1
            max_size = max(max_size, bfs(i, j))
print(cnt)
print(max_size)