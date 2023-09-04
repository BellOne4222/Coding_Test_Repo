from collections import deque

c = int(input()) # 컴퓨터 개수
pair = int(input()) # 연결선 개수
graph = [[] for i in range(c+1)] # 그래프 초기화
visited = [0] * (c+1) # 방문한 컴퓨터인지 표시
for i in range(pair): # 그래프 생성
    s,e = map(int,input().split())
    graph[s] += [e] # s에 e 연결
    graph[e] += [s] # e에 s 연결 -> 양방향
    
queue = deque([1])
visited[1] = 1 # 1번 컴퓨터부터 시작이니 방문 표시
while queue:
    v = queue.popleft()
    for j in graph[v]:
        if visited[j] == 0:
            queue.append(j)
            visited[j] = 1
print(sum(visited) - 1)

