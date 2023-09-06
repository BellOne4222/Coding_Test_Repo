import sys
sys.setrecursionlimit(10000) # 재귀 깊이 설정

t = int(input())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        
        for l in range(4):
            nx = x + dx[l]
            ny = y + dy[l]
            dfs(nx,ny)
        return True
    return False
for _ in range(t):
    m,n,k = list(map(int,input().split()))
    
    graph = [[0] * m for _ in range(n)]
    for i in range(k):
        a,b = map(int,input().split())
        graph[b][a] = 1
    bug = 0    
    for j in range(n):
        for k in range(m):
            if dfs(j,k) == True:
                bug += 1
    print(bug)
        

