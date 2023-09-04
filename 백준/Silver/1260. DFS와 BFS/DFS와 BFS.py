from collections import deque


def dfs(vertex):
    d_visited[vertex] = True
    print(vertex, end=" ")

    for i in graph[vertex]:
        if not d_visited[i]:
            dfs(i)


def bfs(vertex):
    queue = deque([vertex])
    b_visited[vertex] = True
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not b_visited[i]:
                b_visited[i] = True
                queue.append(i)


v, e, s = map(int, input().split())
graph = [[] for _ in range(v + 1)]

for _ in range(e):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

for j in graph:
    j.sort()


d_visited = [False] * (v + 1)
b_visited = [False] * (v + 1)

dfs(s)
print()
bfs(s)
    





