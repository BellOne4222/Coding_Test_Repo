import sys
from collections import deque
    
r, c = map(int, sys.stdin.readline().split())

graph = [list(sys.stdin.readline().rstrip()) for _ in range(r)] 
# [['#', '#', '#', '#'], ['#', 'J', 'F', '#'], ['#', '.', '.', '#'], ['#', '.', '.', '#']]

graph_visited = [[0]*c for _ in range(r)]
fire_visited = [[0]*c for _ in range(r)]

fire_queue = deque()
graph_queue = deque()

for i in range(r):
    for j in range(len(graph[0])):
        if graph[i][j] == "J":
            graph_queue.append([i,j])
            graph_visited[i][j] = 1
        if graph[i][j] == "F":
            fire_queue.append([i,j])
            fire_visited[i][j] = 1
        
        if graph_visited[i][j] == 1 and fire_visited[i][j] == 1:
            break

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs():
    
    # 불 bfs
    while fire_queue:
        cur_x, cur_y = fire_queue.popleft()
        
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            
            if 0 <= nx < r and 0 <= ny < c: 
                if not fire_visited[nx][ny] and graph[nx][ny] != "#":
                    fire_visited[nx][ny] = fire_visited[cur_x][cur_y] + 1
                    fire_queue.append([nx,ny])
    
    # 그래프 bfs            
    while graph_queue:
        cur_x, cur_y = graph_queue.popleft()
        
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            
            if 0 <= nx < r and 0 <= ny < c: 
                if not graph_visited[nx][ny] and graph[nx][ny] != "#":
                    if not fire_visited[nx][ny] or fire_visited[nx][ny] > graph_visited[cur_x][cur_y] + 1:
                        graph_visited[nx][ny] = graph_visited[cur_x][cur_y] + 1
                        graph_queue.append([nx,ny])
            
            else:
                return graph_visited[cur_x][cur_y]
    
    return "IMPOSSIBLE"

print(bfs())
