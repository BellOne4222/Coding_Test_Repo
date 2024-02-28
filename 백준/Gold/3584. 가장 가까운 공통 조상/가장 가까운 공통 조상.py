import sys
sys.setrecursionlimit(10**6)

def dfs(vertex,visited):
    if graph[vertex]:
        visited.append(graph[vertex][0])
        dfs(graph[vertex][0],visited)

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    graph = [[] for _ in range(n + 1)]
    visited_start = []
    visited_end = []
    for i in range(n-1):
        start, end = map(int, sys.stdin.readline().split())
        graph[end].append(start)
    
    start_v, end_v = map(int, sys.stdin.readline().split())
    visited_start.append(start_v)
    visited_end.append(end_v)
    dfs(start_v,visited_start)
    dfs(end_v,visited_end)
            

    parent_vertex = 0

    while True:
        if not visited_start or not visited_end:
            print(parent_vertex)
            break
        
        start_vertex = visited_start.pop()
        end_vertex = visited_end.pop()
        
        if start_vertex != end_vertex:
            print(parent_vertex)
            break
        else:
            parent_vertex = start_vertex
            continue