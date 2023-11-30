import sys  # sys 모듈을 불러옵니다.
from collections import deque

# 입력값을 받아들입니다.
n, m, k, x = map(int, sys.stdin.readline().split())

# 그래프를 구성하기 위한 빈 리스트를 생성합니다.
graph = [[] for _ in range(n + 1)]

# 방문 여부를 나타내는 리스트와, 최단 거리를 기록하는 리스트를 초기화합니다.
visited = [False] * (n + 1)
paths = [0] * (n + 1)

# 간선 정보를 입력받고 그래프를 구성합니다.
for _ in range(m):
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)

# 최초 노드인 x를 시작으로 하는 BFS를 위한 큐와 방문 여부를 표시합니다.
vertex = []
queue = deque()
queue.append(x)
visited[x] = True
    
# BFS를 수행합니다.
while queue:
    v = queue.popleft()  # 큐에서 하나의 노드를 추출합니다.
    for i in graph[v]:  # 현재 노드와 연결된 노드를 순회합니다.
        if not visited[i]:  # 아직 방문하지 않은 노드라면
            visited[i] = True  # 방문 여부를 표시하고
            queue.append(i)  # 큐에 해당 노드를 추가합니다.
            paths[i] = paths[v] + 1  # 최단 거리를 기록합니다.
            if paths[i] == k:  # 최단 거리가 k인 경우 해당 노드를 기록합니다.
                vertex.append(i)

# 결과 출력
if len(vertex) == 0:
    print(-1)  # 경로가 존재하지 않는 경우 -1을 출력합니다.
else:
    vertex.sort()  # 경로가 존재하는 경우 정렬 후 출력합니다.
    for v in vertex:
        print(v, end="\n")  # 해당 노드를 출력합니다.