import sys

r,c = map(int, sys.stdin.readline().split())

grid = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(r)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

change = []

for i in range(r):
    for j in range(c):
        cnt = 0
        if grid[i][j] == "X":
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                if 0 <= nx < r and 0 <= ny < c and grid[nx][ny] == ".":
                    cnt += 1
                elif nx < 0 or ny < 0  or nx >= r or ny >= c:
                    cnt += 1
            
            if cnt >= 3:
                change.append([i,j])

for ch in change:
    x,y = ch[0],ch[1]
    grid[x][y] = "."

# 최소 직사각형 범위 찾기
min_x, min_y = r, c
max_x, max_y = 0, 0

for l in range(r):
    for m in range(c):
        if grid[l][m] == "X":
            min_x = min(min_x, l)
            min_y = min(min_y, m)
            max_x = max(max_x, l)
            max_y = max(max_y, m)

# 최소 직사각형의 좌표 저장
square = [min_x, max_x, min_y, max_y]


for i in range(square[0], square[1] + 1):
    print("".join(grid[i][square[2]:square[3] + 1]))

        

# [['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], 
# ['.', '.', 'X', 'X', '.', '.', '.', 'X', '.', '.'], 
# ['.', 'X', 'X', '.', '.', '.', '.', '.', '.', '.']]  
            