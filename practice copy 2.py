import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]

for i in range(m):
    start, end = map(int, sys.stdin.readline().split())
    
    graph[start].append(end)
    graph[end].append(start)

print(graph)