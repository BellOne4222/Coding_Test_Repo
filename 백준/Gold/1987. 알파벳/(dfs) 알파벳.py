# 참고 : https://sorryhyeon.tistory.com/34

# 입력으로 세로 길이와 가로 길이를 받음
r, c = map(int, input().split())

# 보드의 각 행을 입력 받아 2차원 리스트로 저장
maps = []
for _ in range(r):
    maps.append(list(input()))

ans = 0  # 말이 지날 수 있는 최대 칸 수를 저장할 변수
alphas = set()  # 이미 방문한 알파벳을 추적하는 집합
dx = [-1, 1, 0, 0]  # 상하좌우 이동을 위한 리스트
dy = [0, 0, -1, 1]

# DFS 함수 정의
def dfs(x, y, count):
    global ans
    ans = max(ans, count)  # 말이 이동한 칸 수의 최댓값으로 갱신

    # 상하좌우로 이동하며 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 범위 내에 있고, 이미 방문하지 않은 알파벳인 경우
        if 0 <= nx < r and 0 <= ny < c and not maps[nx][ny] in alphas:
            alphas.add(maps[nx][ny])  # 방문한 알파벳을 집합에 추가
            dfs(nx, ny, count + 1)  # DFS 재귀 호출
            alphas.remove(maps[nx][ny])  # DFS 이후 방문한 알파벳을 집합에서 제거

alphas.add(maps[0][0])  # 시작 지점의 알파벳을 집합에 추가
dfs(0, 0, 1)  # DFS 호출하여 말이 이동할 수 있는 최대 칸 수 계산
print(ans)  # 결과 출력

#DFS를 통해 말이 이동할 수 있는 최대 칸 수를 찾습니다. 재귀적으로 DFS 함수를 호출하면서 상하좌우로 이동하며 
# 이미 방문한 알파벳을 제외하고 가능한 모든 경로를 탐색합니다. 최종적으로 말이 이동할 수 있는 최대 칸 수를 출력합니다.