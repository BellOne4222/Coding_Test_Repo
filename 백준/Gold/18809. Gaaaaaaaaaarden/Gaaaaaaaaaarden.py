from itertools import combinations
from collections import deque

# 입력 받기
N, M, G, R = map(int, input().split())
garden = [list(map(int, input().split())) for _ in range(N)]

# 배양액을 뿌릴 수 있는 땅을 모두 찾음
possible_locations = [(i, j) for i in range(N) for j in range(M) if garden[i][j] == 2]

# 이동 방향 (상, 하, 좌, 우)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# BFS를 사용해 꽃이 피는 개수를 세는 함수
def simulate(green, red):
    queue = deque()
    # 각 셀에 대한 시간 추적
    time = [[-1] * M for _ in range(N)]
    # 각 셀의 상태를 추적하는 배열 (0: 없음, 1: 초록, 2: 빨강, 3: 꽃)
    color = [[0] * M for _ in range(N)]
    flower_count = 0  # 꽃이 핀 개수

    # 초록 배양액의 위치를 큐에 추가하고 초기화
    for idx, (gx, gy) in enumerate(green):
        queue.append((gx, gy, 1, 0))  # 위치, 색상, 시간
        time[gx][gy] = 0
        color[gx][gy] = 1  # 초록 배양액

    # 빨강 배양액의 위치를 큐에 추가하고 초기화
    for idx, (rx, ry) in enumerate(red):
        queue.append((rx, ry, 2, 0))  # 위치, 색상, 시간
        time[rx][ry] = 0
        color[rx][ry] = 2  # 빨강 배양액

    # BFS로 배양액 퍼뜨리기
    while queue:
        x, y, col, t = queue.popleft()

        # 이미 꽃이 핀 경우 더 이상 진행하지 않음
        if color[x][y] == 3:
            continue

        # 상하좌우 인접한 곳으로 확산
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and garden[nx][ny] != 0:
                if time[nx][ny] == -1:  # 아직 방문하지 않은 곳
                    time[nx][ny] = t + 1
                    color[nx][ny] = col
                    queue.append((nx, ny, col, t + 1))
                elif time[nx][ny] == t + 1:  # 동일한 시간에 다른 배양액이 도착한 경우
                    if color[nx][ny] == 1 and col == 2:
                        color[nx][ny] = 3  # 꽃 피우기
                        flower_count += 1
                    elif color[nx][ny] == 2 and col == 1:
                        color[nx][ny] = 3  # 꽃 피우기
                        flower_count += 1

    return flower_count

# 가능한 모든 배치 조합을 탐색
max_flowers = 0
# 초록 배양액을 뿌릴 위치의 모든 조합을 선택
for green_comb in combinations(possible_locations, G):
    # 초록 배양액을 뿌리지 않은 나머지 위치를 선택
    remaining = [loc for loc in possible_locations if loc not in green_comb]
    # 빨강 배양액을 뿌릴 위치의 모든 조합을 선택
    for red_comb in combinations(remaining, R):
        max_flowers = max(max_flowers, simulate(green_comb, red_comb))

# 결과 출력
print(max_flowers)
