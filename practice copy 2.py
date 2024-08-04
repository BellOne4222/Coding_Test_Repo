from collections import deque

# BFS 함수: 배양액이 배치된 위치를 기반으로 꽃의 개수를 계산
def bfs(tlst):
    # [0] 큐와 방문 배열 초기화, 꽃의 수 카운트
    q = deque()
    v = [[0] * (M + 2) for _ in range(N + 2)]
    cnt = 0

    # [1] 큐에 초기 배양액 위치를 추가하고 방문 배열에 기록
    for i in range(TC):
        if tlst[i] == 0:  # 배양액을 뿌리지 않는 경우 건너뛴다
            continue
        ti, tj = lst[i]
        q.append((ti, tj))
        v[ti][tj] = tlst[i]  # 빨간(-1), 초록(+1)으로 표시

    # BFS 탐색을 시작
    while q:
        # 현재 위치에서 배양액을 퍼뜨린다
        ci, cj = q.popleft()

        # 현재 위치에 꽃이 이미 피어 있으면 스킵
        if v[ci][cj] == 25000:
            continue

        # 네 방향 탐색 (상하좌우)
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if arr[ni][nj] == 0 or v[ni][nj] == 25000:
                continue  # 호수이거나 꽃이 이미 피어있으면 스킵

            # 처음 방문하는 경우 (초기값이 0)
            if v[ni][nj] == 0:
                if v[ci][cj] < 0:  # 빨간색 배양액인 경우
                    v[ni][nj] = v[ci][cj] - 1  # 음수로 감소
                    q.append((ni, nj))
                else:  # 초록색 배양액인 경우
                    v[ni][nj] = v[ci][cj] + 1  # 양수로 증가
                    q.append((ni, nj))
            # 이미 기록된 경우, 서로 다른 색의 배양액이 동시에 도달하여 꽃이 피어난 경우
            else:
                if v[ci][cj] < 0:  # 빨간색 배양액인 경우
                    if v[ni][nj] + v[ci][cj] - 1 == 0:
                        cnt += 1
                        v[ni][nj] = 25000  # 꽃이 피어났음을 표시
                else:  # 초록색 배양액인 경우
                    if v[ni][nj] + v[ci][cj] + 1 == 0:
                        cnt += 1
                        v[ni][nj] = 25000  # 꽃이 피어났음을 표시
    return cnt

# DFS 함수: 가능한 배양액 배치를 찾는 백트래킹 함수
def dfs(n, rcnt, gcnt, tlst):
    global ans
    # 모든 땅에 대해 배양액 배치를 결정했을 때
    if n == TC:
        if rcnt == RC and gcnt == GC:
            # 배양액 배치를 기반으로 꽃의 최대 개수 계산
            ans = max(ans, bfs(tlst))
        return

    # 배양액 배치 경우의 수 생성
    dfs(n + 1, rcnt + 1, gcnt, tlst + [-1])  # 빨간 배양액 배치
    dfs(n + 1, rcnt, gcnt + 1, tlst + [1])   # 초록 배양액 배치
    dfs(n + 1, rcnt, gcnt, tlst + [0])       # 배양액을 뿌리지 않는 경우

# 입력 처리
N, M, RC, GC = map(int, input().split())  # 행, 열, 빨간, 초록 배양액 수
arr = [[0] * (M + 2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (M + 2)]

# 배양액을 뿌릴 수 있는 땅의 좌표 리스트 생성
lst = []
for i in range(1, N + 1):
    for j in range(1, M + 1):
        if arr[i][j] == 2:
            lst.append((i, j))
TC = len(lst)

# 가능한 모든 배양액 배치에 대해 최대 꽃 개수 찾기
ans = 0
dfs(0, 0, 0, [])
print(ans)
