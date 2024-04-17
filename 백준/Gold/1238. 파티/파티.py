import heapq

def dijkstra(s):
    # 초기화: 모든 정점까지의 최단 거리를 무한대로 설정
    D = [float('inf')] * (N+1)
    D[s] = 0  # 시작 정점의 거리는 0
    q = []  # 우선순위 큐(최소 힙) 초기화
    heapq.heappush(q, (0, s))  # 시작 정점을 우선순위 큐에 추가
    
    while q:
        dist, now = heapq.heappop(q)  # 큐에서 최소 거리 정점을 추출
        
        if D[now] >= dist:  # 추출된 거리가 현재 기록된 거리보다 크거나 같다면 무시
            for v, val in city[now]:  # 현재 정점에서 이어진 모든 정점을 탐색
                if dist + val < D[v]:  # 새로운 거리가 더 작다면 갱신
                    D[v] = dist + val
                    heapq.heappush(q, (dist + val, v))  # 갱신된 거리와 정점을 큐에 추가
    return D

N, M, X = map(int, input().split())
city = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, t = map(int, input().split())
    city[a].append([b, t])  # 도로 정보를 인접 리스트 형식으로 저장

ans = dijkstra(X)  # X에서 모든 정점까지의 최단 거리 계산
ans[0] = 0  # 0번 마을은 없으므로 0으로 설정 (1-indexed)
for i in range(1, N+1):
    if i != X:
        res = dijkstra(i)  # 각 마을에서 X까지의 최단 거리 계산
        ans[i] += res[X]  # 왕복 시간을 갱신

print(max(ans))  # 최대 왕복 시간 출력