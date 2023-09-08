from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y,standard):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = 1
    while queue:
        cur_x, cur_y = queue.popleft()
        for k in range(4):
            nx = cur_x + dx[k]
            ny = cur_y + dy[k]
            # 범위 내이고, 아직 방문하지 않았고, 그래프의 좌표 값이 기준 높이 보다 높으면
            if 0 <= nx and nx < n and 0 <= ny and ny < n and visited[nx][ny] == 0 and graph[nx][ny] > standard:
                queue.append((nx,ny))
                # 방문 처리
                visited[nx][ny] = 1
                
    

n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

no_chimsu = 0

for height in range(100):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    no_ground = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0 and graph[i][j] > height:
                bfs(i,j,height)
                no_ground += 1
    no_chimsu = max(no_chimsu, no_ground)
print(no_chimsu)
                


                
            
    
    


