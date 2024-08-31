import sys
import heapq

def dijkstra(start):
    queue = []
    
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            c = dist + i[1]  # c는 현재까지의 거리(dist)와 다음 도시로 가는 거리(i[1])의 합
            if c < distance[i[0]]:
                distance[i[0]] = c  # 'cost'가 아닌 'c'로 수정
                heapq.heappush(queue, (c, i[0]))  # 'cost'가 아닌 'c'로 수정

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())

INF = int(1e9)
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    s, e, cost = map(int, sys.stdin.readline().split())
    graph[s].append((e, cost))

start_node, end_node = map(int, sys.stdin.readline().split())

dijkstra(start_node)

print(distance[end_node])
