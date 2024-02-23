import sys
from collections import deque

def bfs(x):
    dy = [1,-1,a,-a,b,-b,a,b]
    queue = deque()
    queue.append(x)
    visited[x] = True
    
    while queue:
        cur_x = queue.popleft()
        
        for i in range(8):
            if i < 6:
                nx = cur_x + dy[i]
            else:
                nx = cur_x * dy[i]
            
            if 0 <= nx < 100000:
                if not visited[nx]:
                    visited[nx] = True
                    queue.append(nx)
                    bridge[nx] = bridge[cur_x] + 1


    
    

a,b,n,m = map(int, sys.stdin.readline().split())

bridge = [0 for _ in range(100001)]
visited = [False for _ in range(100001)]

bfs(n)

print(bridge[m])