def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True

    # 현재 노드와 연결된 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]: # visited[i] = False이면
            dfs(graph, i, visited)

graph = []

visited = [False] * 9

dfs(graph, 1, visited)


from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = []

visited = [False] * 9

bfs(graph, 1, visited)