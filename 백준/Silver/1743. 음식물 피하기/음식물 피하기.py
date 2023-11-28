import sys  # sys 모듈을 불러옵니다.
from collections import deque

# BFS 함수 정의
def bfs(x, y, visited):
    # 상하좌우 방향을 나타내는 리스트
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    # 큐 생성 및 시작 위치 초기화
    queue = deque()
    queue.append([x, y])
    visited[x][y] = True  # 방문한 곳 표시
    trash = 0  # 쓰레기 크기를 나타내는 변수 초기화
    
    # BFS 탐색
    while queue:
        cur_x, cur_y = queue.popleft()
        trash += 1  # 쓰레기 크기 1 증가
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            
            # 인덱스가 범위 내에 있고, 방문하지 않았으며, 쓰레기가 있는 경우
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and path[nx][ny]:
                visited[nx][ny] = True  # 방문한 곳으로 표시
                queue.append([nx, ny])  # 큐에 새로운 위치 추가
    
    return trash  # 최종 쓰레기 크기 반환

# 입력 처리
n, m, k = map(int, sys.stdin.readline().split())
path = [[0] * m for _ in range(n)]  # 쓰레기 위치를 나타내는 리스트 초기화
visited = [[0] * m for _ in range(n)]  # 방문 여부를 나타내는 리스트 초기화
max_trash = 0  # 최대 쓰레기 크기 초기화

# 쓰레기 위치 정보 입력 및 처리
for _ in range(k):
    r, c = map(int, sys.stdin.readline().split())
    path[r - 1][c - 1] = 1  # 쓰레기가 있는 위치 표시

# 모든 위치에 대해 방문하지 않았고 쓰레기가 있는 곳을 탐색하여 최대 쓰레기 크기 찾기
for i in range(n):
    for j in range(m):
        if not visited[i][j] and path[i][j]:
            answer = bfs(i, j, visited)
            max_trash = max(max_trash, answer)

# 최대 쓰레기 크기 출력
print(max_trash)