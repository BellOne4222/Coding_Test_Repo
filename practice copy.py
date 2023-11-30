import sys  # sys 모듈을 불러옵니다.
from collections import deque

n,m,k,x = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
paths = [0] * (n+1)

for _ in range(n):
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start)

vertex = []
queue = deque()
queue.append(x)
visited[x] = True
    
while queue:
    v = queue.popleft()
    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            queue.append(i)
            paths[i] = paths[v] + 1
            if paths[i] == k:
                vertex.append(i)

if len(vertex) == 0:
    print(-1)
else:
    vertex.sort()
    for v in vertex:
        print(v, end = "\n")