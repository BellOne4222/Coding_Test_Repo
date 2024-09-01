import sys
sys.setrecursionlimit(10000)  # 재귀 깊이 제한을 늘려서 깊은 재귀를 처리할 수 있도록 설정

def dfs(graph, v, visited, parent):
    visited[v] = True  # 현재 정점을 방문했음을 표시
    
    for i in graph[v]:  # 현재 정점 v에 인접한 모든 정점 i에 대해 반복
        if not visited[i]:  # 인접 정점 i가 아직 방문되지 않았다면
            if not dfs(graph, i, visited, v):  # 재귀적으로 DFS 수행 (현재 정점을 부모로 설정)
                return False  # 사이클이 발견되면 False 반환
        elif i != parent:
            # 인접 정점 i가 방문되었지만, i가 부모 노드가 아니라면 사이클 존재
            return False
    return True  # 사이클이 없으면 True 반환

case_number = 0  # 테스트 케이스 번호 초기화
while True:
    n, m = map(int, sys.stdin.readline().split())  # 정점의 개수 n과 간선의 개수 m을 입력 받음
    
    if n == 0 and m == 0:  # 입력의 끝을 나타내는 조건 (0 0)인 경우 종료
        break

    case_number += 1  # 테스트 케이스 번호 증가
    graph = [[] for _ in range(n + 1)]  # 그래프를 인접 리스트 형태로 초기화
    visited = [False] * (n + 1)  # 방문 여부를 체크하는 리스트 초기화
    
    # 무방향 그래프 생성
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())  # 각 간선을 입력 받음
        graph[u].append(v)  # u에서 v로 가는 간선 추가
        graph[v].append(u)  # v에서 u로 가는 간선 추가 (무방향)

    tree_count = 0  # 트리의 개수 초기화
    
    # 모든 정점을 돌면서 DFS 탐색
    for i in range(1, n + 1):
        if not visited[i]:  # 정점 i가 방문되지 않았다면 새로운 연결 요소 발견
            if dfs(graph, i, visited, -1):  # DFS를 통해 연결 요소가 트리인지 확인
                tree_count += 1  # 트리인 경우 개수 증가
    
    # 테스트 케이스에 따른 출력
    if tree_count == 0:
        print(f"Case {case_number}: No trees.")
    elif tree_count == 1:
        print(f"Case {case_number}: There is one tree.")
    else:
        print(f"Case {case_number}: A forest of {tree_count} trees.")
