from collections import deque

def find_blocks(grid):
    n = len(grid)  # 지도의 크기 N

    visited = [[False] * n for _ in range(n)]  # 방문 여부를 나타내는 2차원 배열
    blocks = []  # 블록들을 저장할 리스트

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우 방향

    def bfs(row, col):
        queue = deque([(row, col)])  # 큐를 사용하여 BFS 구현
        count = 0  # 블록 내 장애물 개수를 카운트하기 위한 변수

        while queue:
            r, c = queue.popleft()  # 큐에서 현재 위치 꺼내기

            if not visited[r][c] and grid[r][c] == 1:
                visited[r][c] = True  # 현재 위치를 방문으로 처리
                count += 1  # 장애물 개수 카운트

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    # 인접한 위치가 범위 내에 있고 장애물이 있다면 큐에 추가
                    if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and grid[nr][nc] == 1:
                        queue.append((nr, nc))

        return count

    for i in range(n):
        for j in range(n):
            if not visited[i][j] and grid[i][j] == 1:
                block_size = bfs(i, j)  # 새로운 블록을 찾아서 BFS 탐색 시작
                blocks.append(block_size)

    return blocks


# 입력 받기
n = int(input())  # 지도의 크기 N
grid = []
for _ in range(n):
    row = list(map(int, input().strip()))
    grid.append(row)

# 장애물 블록 찾기
result = find_blocks(grid)

# 블록 수와 블록 내 장애물 수 출력
print(len(result))  # 총 블록 수 출력
for count in sorted(result):  # 오름차순으로 정렬하여 출력
    print(count)