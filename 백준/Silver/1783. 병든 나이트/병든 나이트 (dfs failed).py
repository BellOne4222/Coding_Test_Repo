# dfs
n, m = map(int, input().split())

dx = [-2, -1, 1, 2]
dy = [1, 2, 2, 1]

def dfs(x, y, n, m, graph):
    graph[x][y] = True
    moving = 0
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < m and not graph[nx][ny]:
            moving = max(moving, 1 + dfs(nx, ny, n, m, graph))
    graph[x][y] = False
    return moving

moving = 0
for i in range(n):
    for j in range(m):
        graph = [[False] * m for _ in range(n)]  # 새로운 그래프를 만들어서 사용
        moving = max(moving, dfs(i, j, n, m, graph))

print(moving)