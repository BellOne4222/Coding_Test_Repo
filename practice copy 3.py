import sys
import heapq

while True:
    
    cnt = 0
    
    n = int(sys.stdin.readline().rstrip())
    
    if n == 0:
        break
    
    graph = []
    for _ in range(n):
        graph.append(list(map(int,sys.stdin.readline().split())))
    
    heap = []
    
    visited = [[1e9] * n for _ in range(n)]
    
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    visited[0][0] = graph[0][0]
    heapq.heappush(heap,(visited[0][0], 0, 0))
    cnt += 1
    
    while heap:
        distance, x, y = heapq.heappop(heap)
        
        if x == n-1 and y == n-1:
            print("Problem {}: {}".format(cnt,distance))
            break
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n:
                cost = distance + graph[nx][ny]
                if visited[nx][ny] > cost:
                    visited[nx][ny] = distance + graph[nx][ny]
                    
                    if visited[nx][ny] > cost:
                        visited[nx][ny] = distance + graph[nx][ny]
                        heapq.heappush(heap, (distance + graph[nx][ny], nx, ny))
    
    
    
    