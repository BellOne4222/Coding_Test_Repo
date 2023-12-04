import sys

def bfs():
    global moving
    queue = set([(0, 0, board[0][0])]) # 시간 초과를 줄이기 위해 중복되는 곳은 제거

    while queue:
        x, y, z = queue.pop()

        # 말이 지날 수 있는 최대의 칸 초기화
        moving = max(moving, len(z))

        # 상/하/좌/우 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 내에 있고 알파벳이 중복이 안된다면 탐색
            if 0 <= nx < r and 0 <= ny < c and board[nx][ny] not in z:
                queue.add((nx, ny, board[nx][ny] + z))
                print(queue)


r, c = map(int, sys.stdin.readline().split())

board = [list(map(str, sys.stdin.readline().strip())) for _ in range(r)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
moving = 1

bfs()
print(moving)

