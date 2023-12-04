# 참고 : https://aia1235.tistory.com/70

import sys
from collections import deque

def bfs(i, j, puyo_color):
    # 연쇄 여부를 전역 변수로 사용
    global exploding_check
    
    # 같은 색상의 뿌요 개수 초기화
    same_color = 1
    
    # 터트릴 뿌요의 위치를 저장하는 리스트
    explode_locations = []
    
    # 상하좌우 이동을 위한 리스트
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    
    # BFS를 위한 큐 초기화
    queue = deque()
    queue.append([i, j])
    explode_locations.append([i, j])
    visited[i][j] = True
    
    # BFS 수행
    while queue:
        cur_r, cur_c = queue.popleft()
        for k in range(4):  # 변수명 변경(i -> k)으로 인한 수정
            nr = cur_r + dr[k]
            nc = cur_c + dc[k]
            if 0 <= nr < 12 and 0 <= nc < 6:  # 범위 내에 있는지 확인
                if field[nr][nc] == puyo_color:
                    if not visited[nr][nc]:
                        visited[nr][nc] = True
                        queue.append([nr, nc])
                        explode_locations.append([nr, nc])
                        same_color += 1
    
    # 터트릴 뿌요가 4개 이상인 경우 터뜨리고 exploding_check를 True로 변경
    if same_color >= 4:
        for location in explode_locations:
            field[location[0]][location[1]] = "."
        exploding_check = True


r = 12
c = 6

field = []

# 필드 정보 입력
for i in range(r):
    line = list(sys.stdin.readline().rstrip())
    field.append(line)

# 뿌요 색상 정의
colors = ["R", "G", "B", "P", "Y"]

chain = 0  # 연쇄 횟수 초기화

while True:
    exploding_check = False  # 터짐 여부 초기화
    
    visited = [[False for _ in range(c)] for _ in range(r)]  # 방문 여부 초기화
    
    # 모든 위치에 대해 연결된 뿌요 확인
    for x in range(r):
        for y in range(c):
            if field[x][y] in colors:
                color = field[x][y]
                bfs(x, y, color)
    
    # 뿌요들을 아래로 이동시키기
    for i in range(6):
        rotate_queue = deque()
        for j in range(11, -1, -1):
            if field[j][i] != '.':
                rotate_queue.append(field[j][i])
        for j in range(11, -1, -1):
            if rotate_queue:
                field[j][i] = rotate_queue.popleft()
            else:
                field[j][i] = '.'
        
    # 터지는 뿌요가 없을 경우 반복문 종료
    if not exploding_check:
        break
    else:
        chain += 1  # 연쇄 횟수 증가

print(chain)  # 결과 출력