import sys

# 지도의 크기 R, C를 입력 받음
r, c = map(int, sys.stdin.readline().split())

# 지도를 입력 받아 grid에 저장
grid = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(r)]

# 상하좌우 네 방향을 탐색하기 위한 dx, dy 배열
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 잠길 땅의 좌표를 저장할 리스트
change = []

# 지도를 순회하며 잠길 땅을 확인
for i in range(r):
    for j in range(c):
        cnt = 0
        # 현재 위치가 'X'인 경우
        if grid[i][j] == "X":
            # 네 방향을 탐색
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                # 인접한 칸이 바다거나 지도 밖인 경우
                if 0 <= nx < r and 0 <= ny < c and grid[nx][ny] == ".":
                    cnt += 1
                elif nx < 0 or ny < 0 or nx >= r or ny >= c:
                    cnt += 1
            
            # 인접한 세 칸 또는 네 칸이 바다인 경우 잠길 땅으로 표시
            if cnt >= 3:
                change.append([i, j])

# 잠길 땅을 실제로 바다로 변경
for c in change:
    x, y = c[0], c[1]
    grid[x][y] = "."

# 최소 직사각형 범위를 찾기 위한 변수 초기화
min_x, min_y = r, c
max_x, max_y = 0, 0

# 지도를 순회하며 남아 있는 'X'의 최소/최대 좌표를 찾음
for i in range(r):
    for j in range(c):
        if grid[i][j] == "X":
            min_x = min(min_x, i)
            min_y = min(min_y, j)
            max_x = max(max_x, i)
            max_y = max(max_y, j)

# 최소 직사각형의 좌표를 저장
square = [min_x, max_x, min_y, max_y]

# 최소 직사각형 범위에 맞게 지도 출력
for i in range(square[0], square[1] + 1):
    print("".join(grid[i][square[2]:square[3] + 1]))
