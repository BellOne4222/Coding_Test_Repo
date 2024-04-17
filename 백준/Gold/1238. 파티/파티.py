import sys
import heapq

def dijkstra(start):
    # 각 정점까지의 최소 비용을 무한대로 초기화
    distance = [float('inf')] * (n+1)
    # 시작 정점의 거리는 0으로 초기화
    distance[start] = 0
    heap = []
    # 시작 정점을 힙에 추가
    heapq.heappush(heap, (0, start))
    
    while heap:
        # 힙에서 현재 비용이 가장 작은 정점을 추출
        cur_cost, cur_node = heapq.heappop(heap)
        
        # 현재 노드의 기록된 거리보다 추출된 비용이 더 크면 스킵
        if distance[cur_node] < cur_cost:
            continue
        
        # 연결된 정점들을 확인
        for next_node, cost in graph[cur_node]:
            new_cost = cur_cost + cost
            # 새로운 비용이 현재 기록된 비용보다 작으면 업데이트
            if new_cost < distance[next_node]:
                distance[next_node] = new_cost
                heapq.heappush(heap, (new_cost, next_node))
    return distance

# 입력 받기
n, m, x = map(int, sys.stdin.readline().split())
# 그래프 초기화
graph = [[] for _ in range(n+1)]
# 그래프에 간선 정보 저장
for _ in range(m):
    start, end, cost = map(int, sys.stdin.readline().split())
    graph[start].append((end, cost))

# X에서 각 마을까지의 최단 거리 계산
result = dijkstra(x)
result[0] = 0  # 0번 인덱스는 사용되지 않으므로 0으로 설정

# 각 마을에서 X까지의 최단 거리와 X에서 해당 마을까지의 최단 거리 합산
for i in range(1, n+1):
    if i != x:
        Go_To_X = dijkstra(i)
        result[i] += Go_To_X[x]

# 모든 마을에 대해 왕복 시간 중 최대값 출력
print(max(result))