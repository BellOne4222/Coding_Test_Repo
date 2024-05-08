from itertools import permutations, combinations
from collections import deque

# 가능한 이동 방향 (상, 하, 좌, 우)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(green_locations, red_locations, garden, N, M):
    time = [[-1] * M for _ in range(N)]  # 배양액 도달 시간
    color = [[-1] * M for _ in range(N)]  # 배양액 종류 (초록: 0, 빨강: 1)
    q = deque()
    
    # 초록색 배양액의 시작 위치 설정
    for x, y in green_locations:
        q.append((x, y, 0))  # 위치 및 배양액 종류 (초록: 0)
        time[x][y] = 0
        color[x][y] = 0
    
    # 빨간색 배양액의 시작 위치 설정
    for x, y in red_locations:
        q.append((x, y, 1))  # 위치 및 배양액 종류 (빨강: 1)
        time[x][y] = 0
        color[x][y] = 1
    
    flower_count = 0

    while q:
        x, y, current_color = q.popleft()
        
        if color[x][y] == 2:  # 이미 꽃이 피어난 경우
            continue

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < N and 0 <= ny < M and (garden[nx][ny] == 2) and (time[nx][ny] == -1):
                # 이전에 배양액이 도달하지 않은 땅으로 배양액 확산
                time[nx][ny] = time[x][y] + 1
                color[nx][ny] = current_color
                q.append((nx, ny, current_color))
            
            elif 0 <= nx < N and 0 <= ny < M and (garden[nx][ny] == 2) and (time[nx][ny] == time[x][y] + 1):
                # 동시에 도착하여 꽃이 피어난 경우
                if color[nx][ny] != current_color and color[nx][ny] != 2:
                    flower_count += 1
                    color[nx][ny] = 2  # 꽃으로 변경

    return flower_count

def find_max_flowers(garden, fertile_land, G, R, N, M):
    max_flowers = 0

    # 모든 배양액의 배치 조합을 생성
    for green_comb in combinations(fertile_land, G):
        remaining = set(fertile_land) - set(green_comb)
        for red_comb in combinations(remaining, R):
            flowers = bfs(green_comb, red_comb, garden, N, M)
            max_flowers = max(max_flowers, flowers)

    return max_flowers

# 입력 처리
N, M, G, R = map(int, input().split())
garden = [list(map(int, input().split())) for _ in range(N)]

# 배양액을 뿌릴 수 있는 땅 목록 추출
fertile_land = [(i, j) for i in range(N) for j in range(M) if garden[i][j] == 2]

# 최대 꽃의 개수 계산
print(find_max_flowers(garden, fertile_land, G, R, N, M))