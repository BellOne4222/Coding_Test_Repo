from collections import deque
import sys

def zero_one_bfs(start):
    # deque 구조를 사용해 BFS를 수행하는 큐를 초기화
    dequeu = deque([start])
    # 시작 노드의 최소 비용을 0으로 설정
    distance[start] = 0
    
    # 큐에 아이템이 있는 동안 계속 반복
    while dequeu:
        # 큐에서 현재 노드를 꺼냄
        cur_node = dequeu.popleft()
        
        # 현재 노드와 연결된 모든 노드를 확인
        for next_node, cost in graph[cur_node]:
            # 새로 계산된 비용이 기존 비용보다 작을 경우 업데이트
            if distance[cur_node] + cost < distance[next_node]:
                distance[next_node] = distance[cur_node] + cost
                # 비용이 0이면 큐의 앞쪽에, 그렇지 않으면 뒤쪽에 추가
                if cost == 0:
                    dequeu.appendleft(next_node)
                else:
                    dequeu.append(next_node)

# 입력 처리
n, m = map(int, sys.stdin.readline().split())  # 노드와 간선의 수를 입력 받음
graph = [[] for _ in range(n + 1)]  # 각 노드에 연결된 간선 정보를 저장할 리스트 초기화
distance = [float('inf')] * (n + 1)  # 각 노드까지의 최소 비용을 무한대로 초기화

# 간선 정보 입력
for _ in range(m):
    start, end, cost = map(int, sys.stdin.readline().split())
    # 그래프에 양방향 간선과 비용을 추가
    graph[start].append((end, cost))
    graph[end].append((start, cost))

# 0-1 BFS 알고리즘을 시작 노드에서 실행
zero_one_bfs(1)

# 결과 출력
print(distance[n])  # 1번 노드에서 n번 노드까지의 최소 비용 출력