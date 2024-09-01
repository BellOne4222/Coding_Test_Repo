import sys
sys.setrecursionlimit(10000)

def dfs(graph, v, visited, parent):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            # 방문하지 않은 노드를 재귀적으로 방문
            if not dfs(graph, i, visited, v):
                return False
        elif i != parent:
            # 이미 방문한 노드가 현재 노드의 부모가 아니라면 사이클이 존재
            return False
    return True

case_number = 0
while True:
    n, m = map(int, sys.stdin.readline().split())
    
    if n == 0 and m == 0:
        break

    case_number += 1
    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    
    # 단방향 그래프 생성
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)  # 단방향 간선으로 추가
    
    tree_count = 0
    
    # 트리 개수 세기
    for i in range(1, n + 1):
        if not visited[i]:
            if dfs(graph, i, visited, -1):
                tree_count += 1
    
    # 결과 출력
    if tree_count == 0:
        print(f"Case {case_number}: No trees.")
    elif tree_count == 1:
        print(f"Case {case_number}: There is one tree.")
    else:
        print(f"Case {case_number}: A forest of {tree_count} trees.")
