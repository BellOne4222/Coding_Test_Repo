n, m = map(int, input().split())  # 격자판의 행과 열 입력
graph = [[0] * (m + 1) for _ in range(n + 1)]  # 격자판 초기화
count = 0  # 네모 배치의 가짓수를 저장하는 변수

def dfs(x, y):
    global count  # 전역 변수 count 사용

    # 종료 조건: 시작점(1, 1)에서 마지막 행(n)에 도달한 경우
    if (x, y) == (1, n + 1):
        count += 1  # 네모 배치의 가짓수 증가
        return
    
    # 다음 칸으로 이동하는 좌표 설정
    if x == m:  # 열이 마지막에 도달한 경우 다음 행으로 이동
        nx, ny = 1, y + 1
    else:  # 열의 끝이 아니면 다음 열로 이동
        nx, ny = x + 1, y
        
    # x, y에 네모를 놓지 않은 경우의 재귀 호출
    dfs(nx, ny)
    
    # x, y에 네모를 놓을 수 있고 놓는 경우의 재귀 호출
    if graph[y - 1][x] == 0 or graph[y - 1][x - 1] == 0 or graph[y][x - 1] == 0:
        graph[y][x] = 1  # 네모를 놓음
        dfs(nx, ny)  # 다음 칸으로 이동
        graph[y][x] = 0  # 이후의 경우를 위해 네모를 다시 없앰

dfs(1, 1)  # DFS 시작 지점 (1, 1)
print(count)  # 결과 출력: 네모 배치의 가짓수