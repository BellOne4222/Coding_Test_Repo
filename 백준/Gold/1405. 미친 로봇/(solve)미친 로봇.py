import sys

# 입력값을 읽어와서 리스트로 저장합니다.
inputs = list(map(int, sys.stdin.readline().split()))

n = inputs[0]  # 로봇의 이동 횟수
answer = 0     # 단순한 경로의 확률을 저장할 변수

pers = []
# 동서남북으로 이동할 확률을 p 리스트에 저장합니다. 확률 값을 0~1 사이의 값으로 변환하여 저장합니다.
for i in range(1, 5):
    pers.append(inputs[i] * 0.01)

# 로봇의 이동 경로를 표시할 visited 배열을 초기화합니다. (가능한 최대 범위를 고려하여 크기를 설정합니다.)
visited = [[False] * 29 for _ in range(29)]

# 동, 서, 남, 북 방향을 나타내는 리스트
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 깊이 우선 탐색(DFS)을 수행하는 함수
def dfs(x, y, depth, per):
    # per: DFS(깊이 우선 탐색) 과정에서 현재까지의 경로가 단순한 경로를 이루는 확률을 나타냅니다. per은 로봇이 현재까지의 이동에서 단순한 경로를 이룰 확률
    global answer
    visited[x][y] = True  # 현재 위치를 방문했음을 표시

    for i in range(4):  # 동, 서, 남, 북 방향으로 이동을 시도합니다.
        if not visited[x + dx[i]][y + dy[i]]:  # 아직 방문하지 않은 경우
            if depth >= n:  # 주어진 이동 횟수에 도달한 경우
                answer += per * pers[i]  # 단순한 경로일 확률을 누적합니다.
            else:
                # 다음 위치로 이동하며, 이동한 횟수와 확률을 업데이트하여 재귀적으로 탐색합니다.
                dfs(x + dx[i], y + dy[i], depth + 1, per * pers[i])

    visited[x][y] = False  # 이동이 끝났으므로 현재 위치를 다시 방문하지 않은 상태로 되돌립니다.

# 시작 위치에서 DFS를 호출하여 로봇의 이동 경로를 탐색합니다.
dfs(0, 0, 1, 1)

# 모든 가능한 경로에 대한 단순한 경로일 확률이 누적된 answer 값을 출력합니다.
print(answer)