import sys
from collections import deque

def bfs(vertex):
    invite = set()  # 초대받은 친구들을 저장하기 위해 set을 사용합니다.
    depth = 0
    queue = deque()
    queue.append(vertex)
    visited[vertex] = True
    
    while queue:
        depth += 1
        for _ in range(len(queue)):
            v = queue.popleft()
        
            for i in graph[v]:
                if not visited[i]:
                    visited[i] = True
                    queue.append(i)
                    invite.add(i)  # 초대 목록에 추가합니다.
        
        if depth == 2:
            break
    
    # 상근이와 상근이의 친구, 친구의 친구까지 모두를 초대합니다.
    invite.add(1)  # 상근이 자신도 초대합니다.
    invite.update(graph[1])  # 상근이의 친구들을 초대합니다.
    
    print(len(invite) - 1)  # 상근이 자신을 빼고 출력합니다.
            
        
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start)

visited = [False] * (n+1)

bfs(1)