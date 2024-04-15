import sys
from collections import deque

def bfs(start,end):
    queue = deque()
    queue.append(start)
    visited[start] = True
    
    while queue:
        cur = queue.popleft()
        print(cur, end=" ")
        for j in graph[cur]:
            if not visited[j]:
                visited[j] = True
                queue.append(j)
            

road_dict = {}

n,m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]


for _ in range(m):
    start, end, cost = map(int, sys.stdin.readline().split())
    road = str(start) + str(end)
    road_rev = str(end) + str(start)
    road_dict[road] = cost
    road_dict[road_rev] = cost
    
    graph[start].append(end)
    graph[end].append(start)

for i in graph:
    i.sort()

visited = [False] * (n + 1)

bfs(1,n)