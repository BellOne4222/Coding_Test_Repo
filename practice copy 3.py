# 참고 : https://great-park.tistory.com/110
# 3차원 배열 해결법은 생각하지 못했습니다...
# 벽을 뚫은 경우와 안뚫은 경우를 모두 기록

# 시간복잡도는 O(정점 + 간선) = O(V + E) = O(N x M + 4 x N x M) = O(N x M)이 된다
# Vertex(정점)의 개수는 총 N x M개가 있기 때문에 V = N x M이 되고 Edge(간선)의 경우 상, 하, 좌, 우로 총 4개의 선으로 이어져 있기 때문에 E = 4 x N x M이 된다. 시간복잡도가 결국 O(N x M)이 되는 이유는 시간 복잡도를 계산할 때는 계수를 생략하기 때문에 O(5 x N x M)에서의 계수 5를 생략한 O(N x M)이 된다.
# 따라서 각각의 이중 for문에서 bfs를 실행하기 때문에 최종 시간복잡도는 O(N x M) x O(N x M) = O(N ^ 2 x M ^ 2)이 된다.
# 이렇게 되면 만약 N과 M이 각각 최대 개수인 1000이 된다면 O(1000 ^ 2 x 1000 ^ 2) = 1000000000000, 1조가 된다.
# 약 1억 번이 1초로 계산되기 때문에 총 10000초가 걸리게 된다 (시간제한은 2초).
# 그래서 3중 배열로 해야 시간복잡도 문제를 해결 할 수 있다.

import sys
from collections import deque

# BFS 함수 정의
def bfs(x, y):
    dx = [1, -1, 0, 0]  # 상하좌우 이동에 대한 변화량
    dy = [0, 0, 1, -1]

    queue = deque()
    queue.append([x, y, 0])  # 시작점과 함께 벽을 부순 횟수 추가
    path[x][y][0] = 1  # 시작점 방문 표시

    while queue:
        cur_x, cur_y, break_cnt = queue.popleft()  # 현재 위치와 함께 벽을 부순 횟수 가져옴

        if (cur_x, cur_y) == (n - 1, m - 1):  # 목적지에 도달한 경우
            return path[cur_x][cur_y][break_cnt]  # 최단 경로 길이 반환

        for i in range(4):  # 상하좌우에 대해 탐색
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and break_cnt == 0:  # 벽이 있고 아직 벽을 부순 적이 없는 경우
                    path[nx][ny][1] = path[cur_x][cur_y][0] + 1  # 벽을 부수고 다음 위치로 이동
                    queue.append([nx, ny, 1])  # 다음 위치와 함께 벽을 부순 횟수 1 추가

                if graph[nx][ny] == 0 and path[nx][ny][break_cnt] == 0:  # 벽이 없고 아직 방문하지 않은 경우
                    path[nx][ny][break_cnt] = path[cur_x][cur_y][break_cnt] + 1  # 이동하고 다음 위치 방문 표시
                    queue.append([nx, ny, break_cnt])  # 다음 위치와 함께 벽을 부순 횟수 유지

    return -1  # 도달할 수 없는 경우 -1 반환

n, m = map(int, sys.stdin.readline().split())  # 지도의 크기 입력

graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]  # 지도 정보 입력

path = [[[0, 0] for _ in range(m)] for _ in range(n)]  # 방문 여부와 벽을 부순 횟수를 저장할 3차원 리스트 초기화

print(bfs(0, 0))  # 최단 경로 길이 출력


# BFS 탐색:

# BFS 함수를 정의하고, 시작점부터 BFS 탐색을 시작합니다. 초기에는 출발점에서 출발하며, 벽을 부순 횟수를 함께 저장합니다.
# 큐에 시작점을 넣고, 해당 위치를 방문했다는 표시를 합니다.
# 큐가 빌 때까지 다음 과정을 반복합니다.
# 큐에서 현재 위치와 함께 벽을 부순 횟수를 가져옵니다.
# 목적지에 도달했는지 확인하고, 도달했다면 최단 경로 길이를 반환합니다.
# 상하좌우로 인접한 위치에 대해 탐색하며, 이동이 가능한 경우와 벽을 부술 수 있는 경우를 따로 처리합니다.
# 이동 가능한 경우는 벽을 부수지 않은 경우와 벽을 부순 경우로 나누어서 처리합니다. 벽을 부순 경우에는 해당 위치를 큐에 넣고, 벽을 부쉈다는 표시를 합니다.
# 이동 가능한 경우에는 해당 위치를 큐에 넣고, 방문 표시를 합니다.



        
