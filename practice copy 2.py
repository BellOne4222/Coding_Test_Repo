import sys

n,m = map(int,sys.stdin.readline().split())

grid = [[0 for _ in range(m+1)] for _ in range(n+1)]

case = 0 # 첫 번째 줄에 주어진 격자판에서 나올 수 있는, “넴모”들이 올라간 칸이 2 × 2 사각형을 이루지 않는 모든 배치의 가짓수

def dfs(x, y):
    global case
    # 종료 조건
    if (x, y) == (1, n + 1):
        case += 1
        return
    
    if x == m:
        nx, ny = 1, y + 1
    else:
        nx, ny = x + 1, y
        
    # x, y에 네모를 놓지 않은 경우
    dfs(nx, ny)
    
    # x, y에 네모를 놓을 수 있고 놓는 경우
    if grid[y - 1][x] == 0 or grid[y - 1][x - 1] == 0 or grid[y][x - 1] == 0:
        grid[y][x] = 1
        dfs(nx, ny)
        grid[y][x] = 0
        
dfs(1, 1)

print(case)