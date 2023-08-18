def find_obstacles(grid):
    n = len(grid)

    visited = [[False] * n for _ in range(n)]
    
    blocks = [] # 블록 저장할 리스트

    def dfs(row, col):
        if row < 0 or row >= n or col < 0 or col >= n: # 지도 범위가 넘어가면 
            return 0
        if visited[row][col] or grid[row][col] == 0: # 이미 방문을 했거나 도로가 있으면면
            return 0
        
        visited[row][col] = True # 방문 처리
        block_count = 1 # 블록의 장애물 개수

        block_count += dfs(row - 1, col) # 상
        block_count += dfs(row + 1, col) # 하
        block_count += dfs(row, col - 1) # 좌
        block_count += dfs(row, col + 1) # 우

        return block_count

    for i in range(n):
        for j in range(n):
            if not visited[i][j] and grid[i][j] == 1: # 방문을 안했고, 장애물이 있으면
                block = dfs(i, j) # 새로운 블록 탐색
                blocks.append(block) # 블록 내 장애물 찾으면면 추가
    return blocks


n = int(input()) # 지도 크기
grid = [] # 지도
for _ in range(n):
    rows = list(map(int, input().strip()))
    grid.append(rows)

answer = find_obstacles(grid)

print(len(answer)) # 총 블록수
for ans in sorted(answer):
    print(ans) # 오름차순 정렬해서 블록 수 


# 이 코드는 깊이 우선 탐색(DFS)을 활용하여 장애물 블록을 찾습니다. 각 블록을 찾을 때마다 해당 블록에 속하는 장애물의 수를 구하여 리스트에 저장합니다. 마지막으로 블록 수와 블록 내 장애물 수를 출력합니다.