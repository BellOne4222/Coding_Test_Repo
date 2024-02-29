import sys
from collections import deque
    
def bfs(start,graph,visited):
    queue = deque()
    queue.append(start)
    visited[start] = True
    
    while queue:
        cur_path = queue.popleft()
        
        for idx, travel in enumerate(graph[cur_path]):
            if travel and not visited[idx]:
                visited[idx] = True
                queue.append(idx)   
    
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = []

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))
    

travel_path = list(map(int, sys.stdin.readline().split()))
visited = [False] * (n)
start = travel_path[0] - 1

bfs(start,graph,visited)

flag = "YES"

for tp in travel_path:
    if not visited[tp-1]:
        flag = False
    
print(flag)
    
    