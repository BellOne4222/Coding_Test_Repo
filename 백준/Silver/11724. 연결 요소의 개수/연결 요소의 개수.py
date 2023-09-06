import sys

sys.setrecursionlimit(5000)
input = sys.stdin.readline


def dfs(v,depth):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i,depth+1)

n,m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    s,e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)

visited= [False] * (n+1)
cnt = 0

# 1~N번 노드를 각각돌면서
for i in range(1, n + 1):
    if not visited[i]:  # 만약 i번째 노드를 방문하지 않았다면
        if not graph[i]:  # 만약 해당 정점이 연결된 그래프가 없다면
            cnt += 1  # 개수를 + 1
            visited[i] = True  # 방문 처리
        else:  # 연결된 그래프가 있다면
            dfs(i, 0)  # dfs탐색을 돈다.
            cnt += 1  # 개수를 +1

print(cnt)
    
    