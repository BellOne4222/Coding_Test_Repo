from collections import deque

# 상, 하, 좌, 우 이동을 위한 방향 배열
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# Breadth-First Search 함수
def bfs(maps, x, y, visited):
    queue = deque()
    queue.append([x, y])
    visited[x][y] = True
    day = 0
    
    while queue:
        cur_x, cur_y = queue.popleft()
        day += int(maps[cur_x][cur_y])  # 현재 위치의 숫자를 더해줌 (5,6,15,17,18,21,26,27,1,1)
        
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            
            # 맵 범위 내에 있고, 바다가 아니며 방문하지 않은 경우
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
                if maps[nx][ny] != "X" and not visited[nx][ny]:
                    queue.append([nx, ny])
                    visited[nx][ny] = True
    return day

# 주어진 지도에서 모든 섬에 대해 최대 며칠 머무를 수 있는지 계산하는 함수
def solution(maps):
    maps = list(map(list, maps))  # 문자열을 리스트로 변환하여 처리 [['X', '5', '9', '1', 'X'], ['X', '1', 'X', '5', 'X'], ['X', '2', '3', '1', 'X'], ['1', 'X', 'X', 'X', '1']]
    visited = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]  # 방문 여부를 저장하는 배열
    
    result = []  # 각 섬에서의 최대 머무는 일 수를 저장할 리스트
    
    # 모든 지도를 순회하면서 섬을 찾음
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            # 섬이고 아직 방문하지 않은 경우 BFS를 수행하여 최대 머무는 일 수를 찾음
            if maps[i][j] != "X" and not visited[i][j]:
                result.append(bfs(maps, i, j, visited))
    
    result.sort()  # 결과를 오름차순으로 정렬
    
    if result:
        return result
    else:
        return [-1]  # 섬이 없는 경우 -1을 반환
    
    