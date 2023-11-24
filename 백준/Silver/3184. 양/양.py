import sys
from collections import deque

# BFS로 각 영역을 탐색하고 양과 늑대의 수를 세는 함수
def bfs(x, y):
    # 이동 방향 설정 (상, 하, 좌, 우)
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    sheep_cnt, wolf_cnt = 0, 0  # 영역 안의 양과 늑대 수 초기화
    
    if yard[x][y] == "o":  # 현재 위치가 양인 경우 양 수 증가
        sheep_cnt += 1
    
    if yard[x][y] == "v":  # 현재 위치가 늑대인 경우 늑대 수 증가
        wolf_cnt += 1
    
    queue = deque()
    queue.append([x, y])
    visited[x][y] = True
    
    while queue:
        cur_x, cur_y = queue.popleft()
        
        # 네 방향으로 이동하며 영역을 탐색
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            
            # 격자 범위 안에 있고, 방문하지 않았으며 울타리가 아닌 경우
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny] and yard[nx][ny] != "#":
                visited[nx][ny] = True  # 방문 체크
                queue.append([nx, ny])
                
                if yard[nx][ny] == "o":  # 영역 내 양이면 양 수 증가
                    sheep_cnt += 1
    
                if yard[nx][ny] == "v":  # 영역 내 늑대면 늑대 수 증가
                    wolf_cnt += 1
    
    return sheep_cnt, wolf_cnt  # 양과 늑대의 수 반환

r, c = map(int, sys.stdin.readline().split())  # 행과 열 입력

yard = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(r)]  # 격자 입력
visited = [[False for _ in range(c)] for _ in range(r)]  # 방문 여부를 나타내는 리스트

living_sheep_cnt = 0  # 살아있는 양 수
living_wolf_cnt = 0  # 살아있는 늑대 수

# 전체 격자를 탐색하며 각 영역에서 양과 늑대 수를 파악
for i in range(r):
    for j in range(c):
        if yard[i][j] != "#" and not visited[i][j]:  # 울타리가 아니고 방문하지 않은 영역일 경우
            sheep_cnt, wolf_cnt = bfs(i, j)  # BFS를 통해 해당 영역의 양과 늑대 수 파악
            
            if sheep_cnt > wolf_cnt:  # 영역 내 양 수가 늑대 수보다 많으면
                wolf_cnt = 0  # 늑대는 모두 죽음
            else:
                sheep_cnt = 0  # 그렇지 않으면 양은 모두 죽음
            
            living_sheep_cnt += sheep_cnt  # 살아남은 양 수 누적
            living_wolf_cnt += wolf_cnt  # 살아남은 늑대 수 누적

print("{} {}".format(living_sheep_cnt, living_wolf_cnt))  # 살아남은 양과 늑대 수 출력