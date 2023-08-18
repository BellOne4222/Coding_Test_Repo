def find_obstacle(map):
    n = len(map)

    visited = [[False] * n for _ in range(n)]
    
    blocks = [] # 블록 저장할 리스트

    def dfs(row, col):
        if row < 0 or row >= n or col < 0 or col >= n: # 지도 범위가 넘어가면 
            return 0
        if visited[row][col] or map[row][col] == 0: # 이미 방문을 했거나 지도의 구역에 방문했으면
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
            if not visited[i][j] and map[i][j] == 1:
                block = dfs(i, j)
                blocks.append(block)
    return blocks


n = int(input()) # 지도 크기
map = [] # 지도
for _ in range(n):
    map_list = list(map(int, input().strip()))
    map.append(map_list)

obstacles = find_obstacle(map)

print(len(obstacles))
for obstacle in sorted(obstacles):
    print(obstacle)