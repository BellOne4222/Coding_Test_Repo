# bfs 풀이
# 근처 노드를 먼저 탐색을 하며 나아가고, 노드 마다 잘라서 두 구역을 나누고 한 구역의 연결되어있는 노드 개수를 파악하고, 다른 한쪽은 전체 노드 개수에서 빼는 방식 구현
# 최대 영역의 송전탑 개수와 최소 영역의 송전탑 개수 차이 중의 최솟값을 반환하는 방식 구현 중 모르겠어서 풀이 참고

# bfs 견본
# from collections import deque

# def bfs(graph, start, visited):
#     queue = deque([start])
#     visited[start] = True

#     while queue:
#         v = queue.popleft()
#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True

# graph = []

# visited = [False] * 9

# bfs(graph, 1, visited)

from collections import deque

def solution(n, wires):
    answer = 101
    graph = [[] for _ in range(n+1)] 

    for s, e in wires: # 그래프 생성(시작지점, 종료지점), 양방향
        graph[s].append(e)
        graph[e].append(s)

    for s_v, e_v in wires:
        visited = [False] * (n+1) # 모든 노드를 순회할 것이기 때문에 매 순회마다 방문 배열을 만들어줍니다
        q = deque([s_v])
        result = 1
        visited[s_v] = True # 시작 노드
        visited[e_v] = True # s_v에서 시작해서 짜른 한 쪽만 돌고 나머지 영역은 전체 개수 - 탐색한 영역의 개수

        while q:
            v = q.popleft()
            for i in graph[v]:
                if not visited[i]:
                    result += 1 # 연결된 노드 개수(송전탑 개수)
                    q.append(i)
                    visited[i] = True
                    
        # 이 부분 구현이 힘들어서 https://dev-junku.tistory.com/25 참고
        # 최대 영역의 개수와 최소 영역의 개수의 차이 중 최솟값
        min_transmission = min(result, n-result)
        max_transmission = n - min_transmission
        if answer > max_transmission - min_transmission:
            answer = max_transmission - min_transmission

    return answer

print(solution(9,[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))