import sys
from collections import deque

def bfs():
    queue = deque()
    queue.append([0,0])
    visited[0][0] = True
    hour_melting_cheese = 0
    
    while queue:
        cur_x, cur_y = queue.popleft()
        
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            
            if 0 <= nx < r and 0 <= ny < c:
                if not visited[nx][ny]:
                    if graph[nx][ny] == 0:
                        visited[nx][ny] = True
                        queue.append([nx,ny])
                    
                    elif graph[nx][ny] == 1:
                        graph[nx][ny] = 0
                        visited[nx][ny] = True
                        hour_melting_cheese += 1
    
    cheeses.append(hour_melting_cheese)
    return hour_melting_cheese

r,c = map(int, sys.stdin.readline().split())

graph = []

for i in range(r):
    line = list(map(int, sys.stdin.readline().split()))
    graph.append(line)


cheeses = []

time = 0

dx = [1,-1,0,0]
dy = [0,0,1,-1]
 
while True:
    time += 1
    visited = [[False for _ in range(c)] for _ in range(r)]
    melting_cheese = bfs()
    if melting_cheese == 0:
        break

print(time-1)
print(cheeses[-2])

