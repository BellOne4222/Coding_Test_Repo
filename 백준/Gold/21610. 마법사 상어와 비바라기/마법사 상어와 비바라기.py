import sys
N, M = map(int, sys.stdin.readline().split())
basket = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dy = [9, 0, -1, -1, -1, 0, 1, 1, 1]
dx = [9,-1, -1, 0, 1, 1, 1, 0, -1]
cross = [[-1,-1],[-1,1],[1,-1],[1,1]] #대각선 체크용
cloud = [[N-1,0],[N-2,0],[N-1,1],[N-2,1]] # 조건 2
for _ in range(M):
    d, s = map(int, sys.stdin.readline().split())
    visited = [[0]*N for _ in range(N)]
    clouds = []
    
    while cloud :
        y, x = cloud.pop() # 조건 3-3
        ny, nx = (y + dy[d]*s) % N, (x + dx[d]*s) % N # 조건 1 + 조건 3-1
        basket[ny][nx] += 1
        visited[ny][nx] = 1
        clouds.append([ny,nx])

    for ny, nx in clouds:   
        for ly, lx in cross :
            my, mx = ny + ly, nx + lx
            if 0 <= my < N and 0 <= mx < N and basket[my][mx]: # 조건 3-4 
                basket[ny][nx] += 1

    for i in range (N): # 조건 3-5
        for j in range (N):
            if basket[i][j] >= 2 and not visited[i][j]:
                basket[i][j] -= 2
                cloud.append([i,j])

print(sum(map(sum,basket))) # 전체 합을 구해주자