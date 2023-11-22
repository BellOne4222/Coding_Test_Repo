from collections import deque
import sys
input = sys.stdin.readline

# 입력
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# bfs
direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def bfs(x, y):
    graph[x][y] = 0  # 방문한 곳은 0으로 처리하여 중복 방문 방지
    queue = deque([(x, y)])  # 시작 지점을 큐에 추가
    size = 1  # 그림의 크기 초기값 설정
    while queue:
        x, y = queue.popleft()  # 큐에서 좌표 추출
        for dx, dy in direction:  # 상하좌우 탐색
            nx, ny = x + dx, y + dy
            # 범위 내이고 방문하지 않은 곳이라면 탐색
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                graph[nx][ny] = 0  # 방문 처리
                size += 1  # 그림 크기 증가
                queue.append((nx, ny))  # 다음 위치 큐에 추가
    return size  # 그림의 크기 반환

cnt = 0  # 그림의 개수 카운트
max_size = 0  # 가장 큰 그림의 크기 초기화
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:  # 그림이면
            cnt += 1  # 그림 개수 증가
            max_size = max(max_size, bfs(i, j))  # 가장 큰 그림의 크기 갱신

print(cnt)  # 그림의 개수 출력
print(max_size)  # 가장 큰 그림의 크기 출력