import sys

def dfs(cur_city, cost, depth): #  DFS를 통해 가능한 모든 순회 경로를 탐색
    global min_cost
    global start_city
    global n
    
    # 종료 조건: 모든 도시를 방문한 경우
    if depth == n:
        # 시작 도시로 돌아갈 수 있는 경우 최소 비용 업데이트
        for next_city, city_cost in graph[cur_city]:
            if next_city == start_city:
                min_cost = min(min_cost, cost + city_cost)
        return
    
    if visited[cur_city]:
        return
    
    visited[cur_city] = True
    
    for next_city, city_cost in graph[cur_city]:
        if not visited[next_city]:
            dfs(next_city, cost+city_cost, depth + 1)
            visited[next_city] = False
            

n = int(sys.stdin.readline())

# 비용 행렬로 주어진 각 도시간의 비용을 저장
cost_graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 비용 행렬을 그래프로 변환하여 저장합니다. 각 도시에서 출발하여 갈 수 있는 도시와 그에 대한 비용을 저장
graph = [[] for _ in range(n)] 
# 각 도시에서 갈 수 있는 도시와 비용을 저장하는 그래프
# 예시: [[(도시0, 비용), (도시1, 비용)], [(도시0, 비용), (도시2, 비용)], ...]
min_cost = float('INF') # 최소 비용을 저장하는 변수로, 각 DFS 탐색에서 최소 비용을 업데이트

# 비용 행렬을 그래프로 변환
for i in range(n):
    for j in range(n):
        if cost_graph[i][j] != 0:
            graph[i].append([j,cost_graph[i][j]])

# 각 도시에서 출발하는 경우에 대해 DFS 탐색
for k in range(n):
    visited = [False] * n
    start_city = k # : DFS 탐색 시 시작 도시를 저장하는 변수
    dfs(start_city,0,1)

print(min_cost)
