# 회전을 구현하기 위해서 deque를 사용했고, deque에서 append와 popleft를 사용하려고 했는데 rotate라는 내장 함수를 알게 되어서 rotate를 사용해 오른쪽 방향으로 1칸씩 회전하는 것을 구현
# 시간 복잡도 :  O(rows * columns + q * max(rows, columns))
# 사용하려는 grid를 따로 떼서 다시 생성하고 그 안에서 구현하는 방법과 테두리 원소들만 떼서 배열에 넣어서 회전을 하고 최솟값을 반환하는 로직 중에서 후자를 선택
# 회전을 어떻게 구현하는지가 key인것 같은데 rotate로 구현

from collections import deque

# 초기 grid 생성
def solution(rows, columns, queries):
    grid = [[0] * columns for _ in range(rows)]
    k = 0
    result = []
    for i in range(rows):
        for j in range(columns):
            k += 1
            grid[i][j] = k
            
    # grid : [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24], [25, 26, 27, 28, 29, 30], [31, 32, 33, 34, 35, 36]]
    
    # 테두리 원소들을 담을 deque 생성
    border = deque()
    
    # 윗변부터 오른쪽 방향으로 테두리를 deque에 담기
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
        # https://velog.io/@skkumin/Python-deque%EC%82%AC%EC%9A%A9%ED%95%B4%EC%84%9C-%EB%A6%AC%EC%8A%A4%ED%8A%B8-%ED%9A%8C%EC%A0%84%ED%95%98%EA%B8%B0
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


    
        
            
            
        
    