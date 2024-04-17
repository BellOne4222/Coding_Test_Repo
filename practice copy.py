import sys
import heapq

def dijkstra(start):
    
    distance = [float('inf')] * (n+1)
    distance[0] = 0
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
    return distance

n,m,x = map(int,sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    start,end,cost = map(int,sys.stdin.readline().split())
    graph[start].append((end,cost))

result = dijkstra(2)
result[0] = 0


for i in range(1,n+1):
    if i != x:
        Go_To_X = dijkstra(i)
        result[i] += Go_To_X[x] 
        

print(max(result))