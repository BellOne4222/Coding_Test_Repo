# bfs

from collections import deque

n, m = map(int, input().split())

dx = [-2, -1, 1, 2]
dy = [1, 2, 2, 1]

def can_move(x, y, n, m, graph):
    return 0 <= x < n and 0 <= y < m and not graph[x][y]

def bfs(x, y, n, m, graph):
    queue = deque([(x, y, 0)])  # (x, y, 이동 횟수)를 큐에 넣음
    graph[x][y] = True

    while queue:
        x, y, moves = queue.popleft()  # 큐에서 하나를 꺼냄
        max_moves = moves  # 현재까지의 최대 이동 횟수를 업데이트

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if can_move(nx, ny, n, m, graph):
                graph[nx][ny] = True
                queue.append((nx, ny, moves + 1))

    return max_moves

max_moves = bfs(n-1, 0, n, m, [[False] * m for _ in range(n)])  # 가장 왼쪽 아래 칸에서 시작

print(max_moves)