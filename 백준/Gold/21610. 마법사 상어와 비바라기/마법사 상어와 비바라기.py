import sys

# N: 격자의 크기, M: 이동 명령의 수
N, M = map(int, sys.stdin.readline().split())
# 격자에 저장된 물의 양 정보
basket = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 이동 방향 별 dy, dx 설정 (←, ↖, ↑, ↗, →, ↘, ↓, ↙)
dy = [0, -1, -1, -1, 0, 1, 1, 1]
dx = [-1, -1, 0, 1, 1, 1, 0, -1]

# 대각선 방향 체크용 배열
cross = [[-1, -1], [-1, 1], [1, -1], [1, 1]]

# 초기 구름 위치 설정 (조건 2에 의해 구름 생성 위치)
cloud = [[N-1, 0], [N-2, 0], [N-1, 1], [N-2, 1]]

# M번의 이동 명령 처리
for _ in range(M):
    d, s = map(int, sys.stdin.readline().split())  # 이동 방향과 거리 입력
    visited = [[0]*N for _ in range(N)]  # 구름이 지나간 위치를 표시하는 배열
    clouds = []  # 이번 턴에 이동한 구름을 저장할 배열
    
    # 구름 이동
    while cloud:
        y, x = cloud.pop()  # 현재 구름의 위치
        # 구름 이동 후 위치 계산 (경계 넘어갈 때 처리 포함)
        ny, nx = (y + dy[d]*s) % N, (x + dx[d]*s) % N
        basket[ny][nx] += 1  # 구름이 있는 위치에 물의 양 1 증가
        visited[ny][nx] = 1  # 방문 표시
        clouds.append([ny, nx])  # 이동한 구름 위치 저장

    # 물복사버그 마법 적용
    for ny, nx in clouds:
        for ly, lx in cross:
            my, mx = ny + ly, nx + lx
            # 대각선 방향에 물이 있는지 체크 (경계 안쪽인 경우만)
            if 0 <= my < N and 0 <= mx < N and basket[my][mx]:
                basket[ny][nx] += 1  # 물의 양 증가

    # 구름 생성 및 물의 양 조정
    for i in range(N):
        for j in range(N):
            # 바구니에 저장된 물의 양이 2 이상이고, 방00문하지 않은 칸인 경우
            if basket[i][j] >= 2 and not visited[i][j]:
                basket[i][j] -= 2  # 물의 양 2 감소
                cloud.append([i, j])  # 새로운 구름 생성

# 전체 격자에 저장된 물의 양 합계 출력
print(sum(map(sum, basket)))
