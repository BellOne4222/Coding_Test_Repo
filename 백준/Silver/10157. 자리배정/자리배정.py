import sys

# 공연장 크기와 대기번호를 입력받음
c, r = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())

# 좌석을 관리할 그리드와 방문 상태를 저장할 배열을 초기화
grid = [[0 for _ in range(r)] for _ in range(c)]  # 좌석 번호를 저장할 그리드
visited = [[0 for _ in range(r)] for _ in range(c)]  # 방문 여부를 표시할 배열

# 방향을 설정 (우, 하, 좌, 상)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

cur_r = 0  # 현재 행
cur_c = 0  # 현재 열
dir = 0  # 현재 방향 인덱스 (0: 오른쪽, 1: 아래, 2: 왼쪽, 3: 위쪽)

# 대기번호가 좌석 총 수를 초과하는 경우, 좌석이 없음
if r * c < k:
    print(0)
else:
    # 좌석 배정 루프
    for i in range(1, r * c + 1):
        if i == k:
            # 대기번호가 현재 좌석 번호와 일치하면 좌석 위치를 출력
            result = [cur_c + 1, cur_r + 1]
            print(" ".join(map(str, result)))
            break
        else:
            # 현재 좌석에 번호를 배정하고 방문 처리
            grid[cur_c][cur_r] = i
            visited[cur_c][cur_r] = True
            
            # 현재 방향으로 이동
            cur_c += dx[dir]
            cur_r += dy[dir]
            
            # 이동한 좌석이 범위를 벗어나거나 이미 방문한 경우 방향을 변경
            if cur_c < 0 or cur_r < 0 or cur_c >= c or cur_r >= r or visited[cur_c][cur_r]:
                # 원래 자리로 되돌아감
                cur_c -= dx[dir]
                cur_r -= dy[dir]
                
                # 방향을 시계방향으로 변경
                dir = (dir + 1) % 4

                # 새로운 방향으로 이동
                cur_c += dx[dir]
                cur_r += dy[dir]
