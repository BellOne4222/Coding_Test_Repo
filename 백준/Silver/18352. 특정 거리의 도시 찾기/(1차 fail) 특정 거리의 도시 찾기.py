from collections import deque
import sys
input = sys.stdin.readline

n, m, k, x = map(int,input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    s, e = map(int,input().split())
    graph[s].append(e)

visited = [False] * (n+1)

def bfs(start, path):
    vertex = []
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                path += 1
                if path == k:
                    vertex.append(i)
    if len(vertex) == 0:
        print(-1)
    else:
        vertex.sort()
        for ve in vertex:
            print(ve, end='\n')
                
    

bfs(x,0)
