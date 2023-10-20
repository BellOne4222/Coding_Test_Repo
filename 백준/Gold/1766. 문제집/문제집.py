import sys
import heapq

# 입력으로 정점의 개수(n)와 간선의 개수(m)를 받습니다.
n, m = map(int, sys.stdin.readline().rstrip().split())

# 결과를 저장할 리스트를 초기화합니다.
answer = []

# 각 정점의 진입차수(Indegree)를 저장하는 리스트를 초기화합니다.
inDegree = [0 for _ in range(n + 1)]

# 위상 정렬을 위한 큐를 초기화합니다.
queue = []

# 간선 정보를 받아 그래프를 만듭니다.
graph = [[] for _ in range(n + 1)]
for i in range(m):
    first, second = map(int, sys.stdin.readline().rstrip().split())
    graph[first].append(second)
    inDegree[second] += 1

# 진입차수가 0인 정점들을 큐에 추가합니다.
for i in range(1, n + 1):
    if inDegree[i] == 0:
        heapq.heappush(queue, i)

# 위상 정렬 수행
while queue:
    tmp = heapq.heappop(queue)
    answer.append(tmp)

    # 현재 정점과 연결된 정점들의 진입차수를 감소시키고, 진입차수가 0이 되면 큐에 추가합니다.
    for i in graph[tmp]:
        inDegree[i] -= 1
        if inDegree[i] == 0:
            heapq.heappush(queue, i)

# 위상 정렬 결과를 출력합니다.
print(" ".join(map(str, answer)))