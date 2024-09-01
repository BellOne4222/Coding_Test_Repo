import sys
import heapq

def dijkstra(start):
    # 우선순위 큐(최소 힙) 생성
    queue = []
    
    # 시작 노드를 큐에 추가하고, 시작 노드의 거리를 0으로 설정
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    
    while queue:
        # 큐에서 최단 거리가 가장 짧은 노드 정보 꺼내기
        dist, now = heapq.heappop(queue)
        
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        
        # 현재 노드와 연결된 다른 인접 노드들을 확인
        for i in graph[now]:
            c = dist + i[1]  # 현재 노드를 거쳐서 다른 노드로 가는 비용 계산
            if c < distance[i[0]]:  # 만약 계산된 비용이 기존의 비용보다 작으면 갱신
                distance[i[0]] = c  # 최단 거리 갱신
                heapq.heappush(queue, (c, i[0]))  # 갱신된 노드를 우선순위 큐에 추가

# 도시의 개수 N 입력
n = int(sys.stdin.readline().strip())

# 버스의 개수 M 입력
m = int(sys.stdin.readline().strip())

# 무한을 의미하는 값으로 INF 설정
INF = int(1e9)

# 각 도시의 연결 정보를 저장할 그래프 초기화
graph = [[] for _ in range(n+1)]

# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 버스의 정보 입력 받기
for _ in range(m):
    s, e, cost = map(int, sys.stdin.readline().split())
    # 출발 도시 s에서 도착 도시 e로 가는 비용이 cost인 버스 정보 저장
    graph[s].append((e, cost))

# 출발점과 도착점 정보 입력 받기
start_node, end_node = map(int, sys.stdin.readline().split())

# 다익스트라 알고리즘 실행
dijkstra(start_node)

# 출발 도시에서 도착 도시까지 가는 최소 비용 출력
print(distance[end_node])
