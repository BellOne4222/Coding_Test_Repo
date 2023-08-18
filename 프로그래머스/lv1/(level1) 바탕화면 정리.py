def solution(wallpaper):
    row = len(wallpaper)
    col = len(wallpaper[0])
    grid = [[0 for c in range(col)] for r in range(row)] # 2차원 배열 생성
    for r in range(row):
        for c in range(col):
            if wallpaper[r][c] == "#":
                grid[r][c] = 1
    
    files = [] # 파일이 있는 좌표 위치(1인 좌표)를 files에 저장
    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1:
                files.append((i,j))
    drag_x = [] 
    drag_y = []
    for a in range(len(files)):
        drag_x.append(files[a][0])
        drag_y.append(files[a][1])

    drag_start_x = min(drag_x) # 드래그 시작 x좌표는 파일들의 x좌표 중 최소값
    drag_start_y = min(drag_y) # 드래그 시작 y좌표는 파일들의 y좌표 중 최소값
    drag_end_x = max(drag_x) + 1 # 드래그 종료 x좌표는 파일들의 x좌표 중 최대값 +1
    drag_end_y = max(drag_y) + 1 # 드래그 종료 x좌표는 파일들의 x좌표 중 최대값 +1
    
    result = [drag_start_x, drag_start_y, drag_end_x, drag_end_y] # 드래그 시작 좌표, 끝 좌표 반환
    return result