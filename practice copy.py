import sys
from collections import deque

def roll_dice(dice, direction):
    # 주사위 면을 새로운 위치로 업데이트 하는 함수
    n_dice = [0] * 6
    # 주사위를 동, 남, 서, 북 방향으로 굴렸을 때의 새로운 위치를 계산
    if direction == 0:  # 동쪽
        n_dice[0] = dice[3]
        n_dice[1] = dice[1]
        n_dice[2] = dice[0]
        n_dice[3] = dice[5]
        n_dice[4] = dice[4]
        n_dice[5] = dice[2]
    elif direction == 1:  # 남쪽
        n_dice[0] = dice[1]
        n_dice[1] = dice[5]
        n_dice[2] = dice[2]
        n_dice[3] = dice[3]
        n_dice[4] = dice[0]
        n_dice[5] = dice[4]
    elif direction == 2:  # 서쪽
        n_dice[0] = dice[2]
        n_dice[1] = dice[1]
        n_dice[2] = dice[5]
        n_dice[3] = dice[0]
        n_dice[4] = dice[4]
        n_dice[5] = dice[3]
    elif direction == 3:  # 북쪽
        n_dice[0] = dice[4]
        n_dice[1] = dice[0]
        n_dice[2] = dice[2]
        n_dice[3] = dice[3]
        n_dice[4] = dice[5]
        n_dice[5] = dice[1]
    return n_dice

# 이동 방향에 따른 좌표 변경량 (동, 남, 서, 북)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N, M, K = map(int, sys.stdin.readline().rstrip().split())
graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
answer = 0

# 주사위의 초기 상태 설정
now_dice = [1, 2, 3, 4, 5, 6]
now_dice_x = 0
now_dice_y = 0
now_dir = 0

turn = 0
while turn < K:
    # 주사위를 현재 방향으로 한 칸 이동 시도
    new_dice_x = now_dice_x + dx[now_dir]
    new_dice_y = now_dice_y + dy[now_dir]

    # 이동할 칸이 지도 범위를 벗어나면 방향 전환
    if new_dice_x < 0 or new_dice_y < 0 or new_dice_x >= N or new_dice_y >= M:
        now_dir = (now_dir + 2) % 4
        continue

    turn += 1

    # 주사위 굴림
    new_dice = roll_dice(now_dice, now_dir)
    # BFS를 사용해 이동 가능한 칸의 수를 세고 점수 계산
    que = deque()
    is_visited = [[False for _ in range(M)] for _ in range(N)]

    que.append([new_dice_x, new_dice_y])
    is_visited[new_dice_x][new_dice_y] = True
    cnt = 1
    while que:
        now_x, now_y = que.popleft()
        for t in range(4):
            n_x = now_x + dx[t]
            n_y = now_y + dy[t]

            if n_x < 0 or n_y < 0 or n_x >= N or n_y >= M:
                continue
            if is_visited[n_x][n_y] or graph[n_x][n_y] != graph[new_dice_x][new_dice_y]:
                continue
            que.append([n_x, n_y])
            is_visited[n_x][n_y] = True
            cnt += 1
    # 점수 추가
    answer += cnt * graph[new_dice_x][new_dice_y]

    # 주사위 아랫면과 지도의 값 비교 후 방향 조정
    if graph[new_dice_x][new_dice_y] < new_dice[5]:
        now_dir = (now_dir + 1) % 4
    elif graph[new_dice_x][new_dice_y] > new_dice[5]:
        now_dir = now_dir - 1
        if now_dir < 0:
            now_dir = 3

    # 주사위의 위치와 상태를 업데이트
    now_dice_x = new_dice_x
    now_dice_y = new_dice_y
    now_dice = new_dice

# 최종 점수 출력
print(answer)
