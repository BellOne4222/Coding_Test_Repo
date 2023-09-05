# bfs
# (n,m)까지 가는 최단 경로를 구해야하므로 bfs 사용

# dfs가 유리한 경우
# 1. 재귀적인 특징과 백트래킹을 이용하여 모든 경우를 하나씩 전부 탐색하는 경우
# 2. 그래프의 크기가 클 경우
# 3. 최적의 답을 찾는 것이 아닌 경우
# 4. 경로의 특징을 저장해야하는 경우 ex) 경로의 가중치, 이동 과정에서의 제약

# bfs가 유리한 경우
# 1. 최단 거리, 최단 횟수 구하는 경우
# 2. 최적의 답을 찾는 경우, bfs에서는 가장 처음 발견되는 답이 최단 거리
# 3. 탐색의 횟수를 구해야 하는 경우



from collections import deque
n,m = map(int,input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))
    
def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    # 상하좌우
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    while queue:
        x, y = queue.popleft()
        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]
            # 범위 내인지 확인
            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if graph[nx][ny] == 1:
                    # 탐색 실행
                    queue.append((nx,ny))
                    # 다음 칸을 현재 칸에 +1을 해서 거리 표시
                    graph[nx][ny] = graph[x][y] + 1
    return graph[n-1][m-1]

print(bfs(0,0))



