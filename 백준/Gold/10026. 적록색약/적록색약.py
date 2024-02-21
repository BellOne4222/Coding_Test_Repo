import sys
from collections import deque

# BFS 함수 정의
# 현재 셀이 시작 셀과 같은 색상이며 아직 방문하지 않았을 때만 현재 셀을 방문하도록 합니다. 이렇게 하면, BFS는 같은 색상의 연속된 셀들만 방문하게 되므로, 각 구역을 올바르게 식별할 수 있습니다.
def bfs(x, y, arr, visited):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    color = arr[x][y]  # 현재 위치의 색깔
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    
    while queue:
        cur_x, cur_y = queue.popleft()
        
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < N:  # 그리드 범위 내에 있는지 확인
                if arr[nx][ny] == color and not visited[nx][ny]:  # 같은 색이면서 방문하지 않은 경우
                    visited[nx][ny] = True  # 방문 표시
                    queue.append((nx, ny))  # 큐에 추가

# 입력 받기
N = int(sys.stdin.readline())  # 그리드 크기
normal = [list(sys.stdin.readline().strip()) for _ in range(N)]  # 일반적인 경우의 그림
color_weakness = [[y if y != 'G' else 'R' for y in x] for x in normal]  # 적록색약인 경우의 그림

# 방문 여부를 표시할 배열 초기화
normal_visited = [[False]*N for _ in range(N)]
color_weakness_visited = [[False]*N for _ in range(N)]

# 구역의 개수를 카운트할 변수 초기화
normal_cnt = color_weakness_cnt = 0

# 모든 그리드에 대해서 반복하면서 구역의 개수 계산
for i in range(N):
    for j in range(N):
        if not normal_visited[i][j]:  # 일반적인 경우의 그림에 대해 아직 방문하지 않은 경우
            bfs(i, j, normal, normal_visited)  # BFS 실행
            normal_cnt += 1  # 구역의 개수 증가
        if not color_weakness_visited[i][j]:  # 적록색약인 경우의 그림에 대해 아직 방문하지 않은 경우
            bfs(i, j, color_weakness, color_weakness_visited)  # BFS 실행
            color_weakness_cnt += 1  # 구역의 개수 증가

# 결과 출력
print(normal_cnt, color_weakness_cnt)