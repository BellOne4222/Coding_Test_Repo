import sys
import heapq

def dijkstra(start):
    # 우선순위 큐(힙) 초기화
    heap = []
    heapq.heappush(heap, (0, start))  # 시작 노드와 비용을 힙에 추가
    distance[start] = 0  # 시작점의 최소 비용을 0으로 설정
    
    # 힙에 원소가 있는 동안 반복
    while heap:
        cur_cost, cur_node = heapq.heappop(heap)  # 현재 비용이 가장 낮은 노드 선택
        
        # 현재 노드의 처리된 최소 비용이 이미 현재 비용보다 작은 경우, 스킵
        if distance[cur_node] < cur_cost:
            continue
        
        # 현재 노드와 연결된 모든 노드를 순회
        for next_node, cost in graph[cur_node]:
            new_cost = cur_cost + cost  # 다음 노드로의 새로운 총 비용 계산
            # 새로운 총 비용이 기존에 계산된 비용보다 작은 경우, 업데이트 및 힙에 추가
            if new_cost < distance[next_node]:
                distance[next_node] = new_cost
                heapq.heappush(heap, (new_cost, next_node))


# 입력 처리
n, m = map(int, sys.stdin.readline().split())  # 노드와 간선의 수 입력 받기
graph = [[] for _ in range(n + 1)]  # 각 노드에 연결된 간선 정보를 저장할 리스트 초기화
distance = [float('inf')] * (n + 1)  # 각 노드까지의 최소 비용을 무한대로 초기화

# 각 간선 정보 입력 받기
for _ in range(m):
    start, end, cost = map(int, sys.stdin.readline().split())
    graph[start].append((end, cost))  # 시작점에서 도착점까지 비용을 그래프에 추가
    graph[end].append((start, cost))  # 양방향 그래프이므로 반대 방향도 추가

# 다익스트라 알고리즘 실행
dijkstra(1)

# 결과 출력
print(distance[n])  # 1번 노드에서 n번 노드까지의 최소 비용 출력