# dfs로 접근했지만 실패

def solution(land):
    def dfs(row, col, current_sum):
        if row == len(land):
            nonlocal max_score
            max_score = max(max_score, current_sum)
            return
        
        for j in range(len(land[0])):
            if j != col:  # 이전 행에서의 인덱스와 다른 열을 선택
                dfs(row + 1, j, current_sum + land[row][j])
    
    max_score = 0
    for i in range(len(land[0])):
        dfs(0, i, land[0][i])
    
    return max_score