from collections import deque

dx = [-1, 1, 0, 0]  # x축 이동을 위한 리스트
dy = [0, 0, 1, -1]  # y축 이동을 위한 리스트

# 너비 우선 탐색(BFS) 함수
def bfs(i, j, graph, costs):
    queue = deque()
    queue.append((i, j))
    while queue:
        x, y = queue.popleft()
        for i in range(4):  # 현재 위치에서 4가지 방향으로의 이동 시도
            nx = x + dx[i]
            ny = y + dy[i]
            # 다음 위치가 동굴 범위 내에 있고, 다음 위치로 이동했을 때의 비용이 현재까지의 비용보다 적을 경우
            if 0 <= nx < n and 0 <= ny < n:
                if costs[nx][ny] > costs[x][y] + graph[nx][ny]:
                    costs[nx][ny] = costs[x][y] + graph[nx][ny]
                    queue.append((nx, ny))

count = 1
while True:
    n = int(input())  # 동굴의 크기
    if n == 0:  # 입력 종료 조건
        break
    graph = []  # 동굴의 각 칸에 있는 도둑루피 크기를 저장할 리스트
    costs = [[int(1e9)] * n for _ in range(n)]  # 각 칸까지 이동하는데 필요한 최소 비용
    for _ in range(n):
        graph.append(list(map(int, input().split())))

    costs[0][0] = graph[0][0]  # 시작점의 비용 초기화
    bfs(0, 0, graph, costs)  # BFS를 통한 최소 비용 계산
    print(f'Problem {count}: {costs[n - 1][n - 1]}')  # 최소 비용 출력
    count += 1