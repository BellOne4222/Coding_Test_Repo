# 참고 : https://smin1620.tistory.com/319

import sys
from collections import deque

def bfs(x, y, z):
    # 상하좌우, 위아래를 이동하기 위한 배열
    dx = [0, 0, 0, 0, 1, -1]
    dy = [0, 0, 1, -1, 0, 0]
    dz = [1, -1, 0, 0, 0, 0]
    
    # 큐 생성 및 시작점 추가
    queue = deque()
    queue.append((x, y, z, 0))
    
    # BFS 탐색
    while queue:
        cur_x, cur_y, cur_z, cur_time = queue.popleft()
        
        # 현재 위치에서 6방향으로 이동
        for i in range(6):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            nz = cur_z + dz[i]
            
            # 상범 빌딩의 범위 내에 있고, 방문하지 않았고, 이동 가능한 공간인 경우
            if 0 <= nx < l and 0 <= ny < r and 0 <= nz < c:
                if visited[nx][ny][nz] == False and buildings[nx][ny][nz] == '.':
                    visited[nx][ny][nz] = True
                    queue.append((nx, ny, nz, cur_time + 1))
                # 출구에 도착한 경우
                elif buildings[nx][ny][nz] == 'E' and visited[nx][ny][nz] == False:
                    return 'Escaped in ' + str(cur_time + 1) + ' minute(s).'
    
    # 탈출 불가능한 경우
    return 'Trapped!'

while True:
    l, r, c = map(int, sys.stdin.readline().split())
    if l == 0 and r == 0 and c == 0:
        break
    
    buildings = []
    # 빌딩 정보 입력
    for i in range(l):
        buildings.append([list(sys.stdin.readline().strip()) for _ in range(r)])
        # 각 층 사이 빈 줄 입력
        sys.stdin.readline()
        
    # 방문 여부를 저장할 배열 초기화
    visited = [[[False] * c for _ in range(r)] for _ in range(l)]
    
    # 시작 지점 탐색
    for j in range(l):
        for k in range(r):
            for m in range(c):
                if buildings[j][k][m] == 'S':
                    visited[j][k][m] = True
                    # BFS 호출하여 결과 출력
                    print(bfs(j, k, m))
                    break