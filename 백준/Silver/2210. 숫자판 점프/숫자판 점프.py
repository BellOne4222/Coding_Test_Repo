import sys

def dfs(x, y, nums):
    if len(nums) == 6:
        comb_nums.add(tuple(nums))  # 리스트를 튜플로 변환하여 집합에 저장
        return 
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < 5 and 0 <= ny < 5:
            nums.append(board[nx][ny])
            dfs(nx, ny, nums)
            nums.pop()  # 이전 상태로 복원

# 입력 처리
board = [list(map(int, sys.stdin.readline().split())) for _ in range(5)]

# 중복을 방지하기 위해 집합 사용
comb_nums = set()

# 모든 위치에서 DFS 시작
for i in range(5):
    for j in range(5):
        dfs(i, j, [board[i][j]])

# 결과 출력
print(len(comb_nums))