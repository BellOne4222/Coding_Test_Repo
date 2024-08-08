import sys

def dfs(x,y,nums):
    if len(nums) == 6:
        if nums not in comb_nums:
            comb_nums.append(nums)
        return 
    
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < 5 and 0 <= ny < 5:
            nums.append(board[nx][ny])
            dfs(nx, ny, nums)
    

board = [list(map(int, sys.stdin.readline().split())) for _ in range(5)]

comb_nums = []

for i in range(5):
    for j in range(5):
        nums = []
        nums.append(board[i][j])
        dfs(i,j,nums)

print(comb_nums)