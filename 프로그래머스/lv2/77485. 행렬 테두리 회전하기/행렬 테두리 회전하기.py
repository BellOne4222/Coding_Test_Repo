from collections import deque

def solution(rows, columns, queries):
    grid = [[0] * columns for _ in range(rows)]
    k = 0
    result = []
    for i in range(rows):
        for j in range(columns):
            k += 1
            grid[i][j] = k
            
    # grid : [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24], [25, 26, 27, 28, 29, 30], [31, 32, 33, 34, 35, 36]]
    
    border = deque()
    
    
    for l in queries:
        r1, c1, r2, c2 = l[0], l[1], l[2], l[3]
        
        # 사각형 윗변
        for m in range(c1-1,c2):
            border.append(grid[r1 -1][m])
        
        # 사각형 오른쪽 변
        for m in range(r1,r2):
            border.append(grid[m][c2-1])
        
        # 사각형 밑변
        for m in range(c2-2,c1-2,-1):
            border.append(grid[r2-1][m])
        
        # 사각형 왼쪽 변
        for m in range(r2 - 2,r1 - 1,-1):
            border.append(grid[m][c1 - 1])
        
        border.rotate(1) # 양수일 때는 오른쪽 회전, 음수일 때는 왼쪽 회전
        result.append(min(border))
        
        # 회전한 배열을 원래 배열에 적용
        for n in range(c1 - 1, c2):
            grid[r1 - 1][n] = border.popleft()

        for n in range(r1, r2):
            grid[n][c2 - 1] = border.popleft()

        for n in range(c2 - 2, c1 - 2, -1):
            grid[r2 - 1][n] = border.popleft()

        for n in range(r2 - 2, r1 - 1, -1):
            grid[n][c1 - 1] = border.popleft()
    
    return result


    
        
            
            
        
    