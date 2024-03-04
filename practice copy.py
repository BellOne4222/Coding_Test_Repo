import sys

def dfs(cur_city, cost, depth):
    global min_cost
    global start_city
    global n
    
    # 종료조건
    if depth == n:
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

cost_graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

graph = [[] for _ in range(4)] 
# [[[1, 10], [2, 15], [3, 20]], [[0, 5], [2, 9], [3, 10]], [[0, 6], [1, 13], [3, 12]], [[0, 8], [1, 8], [2, 9]]]
min_cost = float('INF')

for i in range(n):
    for j in range(n):
        if cost_graph[i][j] != 0:
            graph[i].append([j,cost_graph[i][j]])

for k in range(n):
    visited = [False] * n
    start_city = k
    dfs(start_city,0,1)

