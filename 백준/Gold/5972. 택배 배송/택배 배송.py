import sys
import heapq

def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))
    distance[start] = 0
    
    while heap:
        cur_cost, cur_node = heapq.heappop(heap)
        
        if distance[cur_node] < cur_cost:
            continue
        
        for next_node, cost in graph[cur_node]:
            new_cost = cur_cost + cost
            if new_cost < distance[next_node]:
                distance[next_node] = new_cost
                heapq.heappush(heap, (new_cost, next_node))


n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
distance = [float('inf')] * (n + 1)

for _ in range(m):
    start, end, cost = map(int, sys.stdin.readline().split())
    graph[start].append((end, cost))
    graph[end].append((start, cost))  # 양방향 그래프 처리

dijkstra(1)

print(distance[n])