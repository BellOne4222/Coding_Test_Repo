from collections import deque

# 상하좌우 방향 이동을 위한 dx와 dy 리스트를 정의합니다.
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 함수를 정의합니다. 특정 높이를 기준으로 지역을 탐색하며 연결된 덩어리를 찾습니다.
def bfs(x, y, standard):
    queue = deque()  # 큐를 생성하여 BFS를 위한 초기 설정을 합니다.
    queue.append((x, y))  # 시작점을 큐에 추가합니다.
    visited[x][y] = 1  # 방문한 지점을 표시합니다.

    while queue:  # 큐가 빌 때까지 반복합니다.
        cur_x, cur_y = queue.popleft()  # 큐에서 현재 위치를 꺼냅니다.

        for k in range(4):  # 상하좌우 방향을 탐색합니다.
            nx = cur_x + dx[k]
            ny = cur_y + dy[k]

            # 범위 내에 있고, 아직 방문하지 않았으며, 기준 높이보다 높은 경우에만 처리합니다.
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and graph[nx][ny] > standard:
                queue.append((nx, ny))  # 다음 위치를 큐에 추가합니다.
                visited[nx][ny] = 1  # 방문 처리를 합니다.

# 입력 받기
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

no_chimsu = 0  # 결과값으로 출력할 최대 침수 지역 개수를 저장합니다.

# 높이를 0부터 99까지 증가시키며 모든 높이에 대해 침수 지역을 계산합니다.
for height in range(100):
    visited = [[0 for _ in range(n)] for _ in range(n)]  # 방문 여부 초기화
    no_ground = 0  # 현재 높이에서의 침수 지역 개수를 저장할 변수를 초기화합니다.

    # 모든 지역을 탐색하며, 해당 높이보다 높으면 BFS를 수행합니다.
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0 and graph[i][j] > height:
                bfs(i, j, height)
                no_ground += 1  # BFS로 연결된 덩어리의 개수를 증가시킵니다.

    no_chimsu = max(no_chimsu, no_ground)  # 최대 침수 지역 개수를 업데이트합니다.

print(no_chimsu)  # 결과 출력