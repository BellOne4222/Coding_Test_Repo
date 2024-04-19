import sys
from collections import deque

def move_dice(dice, direction):
    new_dice = [0] * 6
    
    # 주사위 굴리기: 방향에 따라 주사위의 각 면이 새로운 위치로 이동
    if direction == 0:  # 동쪽
        new_dice[0] = dice[3]
        new_dice[1] = dice[1]
        new_dice[2] = dice[0]
        new_dice[3] = dice[5]
        new_dice[4] = dice[4]
        new_dice[5] = dice[2]
        
    elif direction == 1:  # 서쪽
        new_dice[0] = dice[2]
        new_dice[1] = dice[1]
        new_dice[2] = dice[5]
        new_dice[3] = dice[0]
        new_dice[4] = dice[4]
        new_dice[5] = dice[3]
        
    elif direction == 2:  # 남쪽
        new_dice[0] = dice[1]
        new_dice[1] = dice[5]
        new_dice[2] = dice[2]
        new_dice[3] = dice[3]
        new_dice[4] = dice[0]
        new_dice[5] = dice[4]
        
    elif direction == 3:  # 북쪽
        new_dice[0] = dice[4]
        new_dice[1] = dice[0]
        new_dice[2] = dice[2]
        new_dice[3] = dice[3]
        new_dice[4] = dice[5]
        new_dice[5] = dice[1]
        
    return new_dice

n, m, k = map(int, sys.stdin.readline().strip().split())
graph = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)] 

total_score = 0

cur_dice = [1, 2, 3, 4, 5, 6]
cur_x, cur_y = 0, 0
cur_direction = 0 # 동쪽

move_cnt = 0

# 동서남북 이동 벡터 설정
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

while move_cnt < k:
    # 주사위를 이동 방향에 따라 한 칸 굴러간다
    next_x, next_y = cur_x + dx[cur_direction], cur_y + dy[cur_direction]
    
    # 주사위가 지도 바깥으로 나가려 할 경우 방향을 반대로 하고 다음 이동을 시도
    if next_x < 0 or next_y < 0 or next_x >= n or next_y >= m:
        cur_direction = (cur_direction + 1) % 2 + 2 * (cur_direction // 2)  # 반대 방향으로 전환
        continue
    
    move_cnt += 1
    
    new_dice = move_dice(cur_dice, cur_direction)
    
    # BFS를 사용해 연속적인 동일 숫자의 칸을 탐색
    queue = deque()
    visited = [[False for _ in range(m)] for _ in range(n)]
    queue.append([next_x, next_y])
    visited[next_x][next_y] = True
    c = 1
    
    while queue:
        cur_bfs_x, cur_bfs_y = queue.popleft()
        
        for i in range(4):
            nx, ny = cur_bfs_x + dx[i], cur_bfs_y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] == graph[next_x][next_y]:
                queue.append([nx, ny])
                visited[nx][ny] = True
                c += 1
    
    # 점수 계산: 현재 칸의 숫자와 탐색된 칸의 개수를 곱함
    total_score += (graph[next_x][next_y] * c)
    
    # 주사위의 아랫면과 칸의 숫자를 비교하여 이동 방향 결정
    a = new_dice[5]
    b = graph[next_x][next_y]
    
    if a > b:
        if cur_direction == 0:
            cur_direction = 2
        elif cur_direction == 1:
            cur_direction = 3
        elif cur_direction == 2:
            cur_direction = 1
        elif cur_direction == 3:
            cur_direction = 0
    elif a < b:
        if cur_direction == 0:
            cur_direction = 3
        elif cur_direction == 1:
            cur_direction = 2
        elif cur_direction == 2:
            cur_direction = 0
        elif cur_direction == 3:
            cur_direction = 1
    
    # 현재 위치와 주사위 상태 업데이트
    cur_x, cur_y, cur_dice = next_x, next_y, new_dice

print(total_score)
