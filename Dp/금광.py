# 이것이 취업을 위한 코딩테스트다 p.375 금광

n = 3
m = 4

grid = [1,3,3,2,2,1,4,1,0,6,4,7]

dp_table = [] # [[1, 3, 3, 2], [2, 1, 4, 1], [0, 6, 4, 7]]
idx = 0
for i in range(n):
    dp_table.append(grid[idx:idx + m])
    idx += m

for j in range(1,m): # 열
    for i in range(n): # 행
        # 왼쪽 위에서 오는 경우
        if i == 0:
            left_up = 0
        else:
            left_up = dp_table[i-1][j-1]
        
        # 왼쪽 아래에서 오는 경우
        if i == n-1:
            left_down = 0
        else:
            left_down = dp_table[i+1][j-1]
        
        # 왼쪽에서 오는 경우
        left = dp_table[i][j-1]
        dp_table[i][j] = dp_table[i][j] + max(left_up,left,left_down)

gold = 0

for i in range(n):
    gold = max(gold, dp_table[i][m-1])

print(gold)


