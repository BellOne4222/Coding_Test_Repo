import sys
import heapq

def dijkstra(start):
    queue = []
    
    heapq.heappush(queue,(0,start))
    distance[start] = 0
    
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            c = dist + i[1]
            if c < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue,(cost,i[0]))


n = int(sys.stdin.readline())

m = int(sys.stdin.readline())

INF = int(1e9)

graph = [[] for _ in range(n+1)]

distance = [INF] * (n+1)

for _ in range(m):
    s, e, cost = map(int, sys.stdin.readline().split())
    
    graph[s].append((e,cost))

start_node, end_node = map(int, sys.stdin.readline().split())

dijkstra(start_node)

print(distance)
