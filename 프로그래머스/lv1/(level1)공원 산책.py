# 1. 2중 배열로 grid를 표현해야한다.
# 2. 방향에 따른 row, col 변화를 미리 저장해 놓는다.
# 3. 검사는 new_사용해서 진행, curr_을 함부로 바꾸지 않는다.
# 4. loop과 offset을 사용해서 쭉 이동하는거 확인

def solution(park, routes):
    ROW, COL = len(park), len(park[0]) 
    grid = [[0 for c_idx in range(COL)] for r_idx in range(ROW)] # 공원 배열 생성
    curr_row, curr_col = 0, 0
    for r_idx in range(ROW):
        for c_idx in range(COL):
            if park[r_idx][c_idx] == "X":
                grid[r_idx][c_idx] = 1
            elif park[r_idx][c_idx] == "S":
                curr_row, curr_col = r_idx, c_idx
    
    dirs = {"N":(-1,0), "S":(1,0), "E":(0,1), "W":(0,-1)}
    for route in routes:
        direction, distance = route.split()
        dir_row, dir_col = dirs[direction]
        is_valid = True

        for offset in range(1, int(distance) + 1):
            new_row, new_col = curr_row + dir_row * offset, curr_col + dir_col * offset
            if new_row in range(ROW) and new_col in range(COL) and grid[new_row][new_col] == 0:
                pass
            else:
                is_valid = False
                break
        if is_valid:
            curr_row, curr_col = new_row, new_col
    
    return[curr_row, curr_col]

# 참고
def solution(park, routes):

    x, y = 0, 0  # 시작점
    w, h = len(park[0]), len(park)  # 가로, 세로
    op = {"N":(-1,0), "S":(1,0), "W":(0,-1), "E":(0,1)}
    
    # 시작점
    for i in range(h):
        for j in range(w):
            if park[i][j]=="S":
                x, y = i, j
                break
        
    # 좌표이동
    for r in routes:
        d, n = r.split(" ") # 방향, 이동횟수
        dx, dy = x, y  # 현재위치
        
        for i in range(int(n)):
            # 이동할 위치
            nx = x + op[d][0]
            ny = y + op[d][1]
        
            if 0<=nx<=h-1 and 0<=ny<=w-1 and (park[nx][ny]!="X"):
                x, y = nx, ny
                    
            else:
                x, y = dx, dy
                break

    return (x,y)