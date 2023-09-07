from collections import deque

m,n,k = map(int,input().split())

graph = [[0 for _ in range(n)] for _ in range(m)]



def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    etc = 1
    while queue:
        s,e = queue.popleft()
        for o in range(4):
            nx = e + dx[o]
            ny = s + dy[o]
            if 0 <= nx and nx < n and 0 <= ny and ny < m:
                if graph[ny][nx] == 0:
                    graph[ny][nx] = 1
                    queue.append((ny,nx))
                    etc += 1
    return etc
                   
for _ in range(k):
    x1,y1,x2,y2 = map(int,input().split())
    for i in range(y1,y2):
        for j in range(x1,x2):
            graph[i][j] += 1

blank = []            
            
for k in range(m):
    for l in range(n):
        if graph[k][l] == 0:
            graph[k][l] += 1
            blank.append(bfs(k,l))

blank.sort()
print(len(blank))
for p in blank:
    print(p)
            
        