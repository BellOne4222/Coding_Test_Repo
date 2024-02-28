import sys

# 우리는 재귀적인 탐색을 통해 각 노드의 부모를 추적할 것입니다.
# 재귀 호출 제한을 높여 스택 오버플로우를 방지합니다.
sys.setrecursionlimit(10**6)

# 깊이 우선 탐색 함수를 정의합니다.
# 이 함수는 각 노드의 부모를 따라가며 방문하는 노드를 기록합니다.
def dfs(vertex, visited):
    if graph[vertex]:  # 노드가 자식을 가지고 있다면
        visited.append(graph[vertex][0])  # 그 자식을 방문 리스트에 추가하고
        dfs(graph[vertex][0], visited)  # 해당 자식 노드로 이동하여 재귀 호출합니다.

# 테스트 케이스의 개수를 입력받습니다.
t = int(sys.stdin.readline())

# 각 테스트 케이스에 대해 반복합니다.
for _ in range(t):
    n = int(sys.stdin.readline())  # 트리를 구성하는 노드의 수를 입력받습니다.
    graph = [[] for _ in range(n + 1)]  # 트리의 인접 리스트를 초기화합니다.

    # 트리를 구성하는 간선 정보를 입력받습니다.
    for i in range(n-1):
        start, end = map(int, sys.stdin.readline().split())
        graph[end].append(start)  # 자식 노드를 부모 노드에 연결합니다.
    
    # 가장 가까운 공통 조상을 찾을 두 노드를 입력받습니다.
    start_v, end_v = map(int, sys.stdin.readline().split())

    visited_start = [start_v]  # 시작 노드의 방문 리스트를 초기화합니다.
    visited_end = [end_v]  # 끝 노드의 방문 리스트를 초기화합니다.
    
    dfs(start_v, visited_start)  # 시작 노드에서 깊이 우선 탐색을 시작합니다.
    dfs(end_v, visited_end)  # 끝 노드에서 깊이 우선 탐색을 시작합니다.

    parent_vertex = 0  # 초기 가장 가까운 공통 조상을 설정합니다.

    # 두 노드의 방문 리스트를 비교하면서 가장 가까운 공통 조상을 찾습니다.
    while True:
        if not visited_start or not visited_end:  # 어느 한 쪽의 방문 리스트가 끝났다면
            print(parent_vertex)  # 현재 가장 가까운 공통 조상을 출력합니다.
            break
        
        start_vertex = visited_start.pop()  # 시작 노드에서 방문한 노드를 꺼냅니다.
        end_vertex = visited_end.pop()  # 끝 노드에서 방문한 노드를 꺼냅니다.
        
        if start_vertex != end_vertex:  # 두 노드가 같지 않다면
            print(parent_vertex)  # 현재 가장 가까운 공통 조상을 출력하고 종료합니다.
            break
        else:
            parent_vertex = start_vertex  # 두 노드가 같다면 현재 노드를 가장 가까운 조상으로 갱신하고 계속합니다.
            continue