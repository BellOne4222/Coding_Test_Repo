from collections import deque

def solution(edges):
    # 정점의 번호, 도넛, 막대, 8자

    v = max(max(edges))

    visited = [False] * (v+1)

    graph = [[] for _ in range(v+1)] # [[], [1, 1, 2], [3, 1], [2, 4], [3]]

    for i in range(len(edges)):
        start, end = edges[i][0], edges[i][1]
        graph[start].append(end)
        graph[end].append(start)
    

    def bfs(vertex):
        queue = deque()
        visited[vertex] = True

        while queue:
            v = queue.popleft()
            print(v, end = " ")
            for i in graph[v]:
                if not visited[i]:
                    visited[i] = True
                    queue.append(i)
    
    bfs(edges[0][0])

print(solution([[2, 3], [4, 3], [1, 1], [2, 1]]))