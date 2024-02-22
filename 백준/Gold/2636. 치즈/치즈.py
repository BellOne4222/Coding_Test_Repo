import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))

dx = [1,-1,0,0]
dy = [0,0,1,-1]
ans = []

def bfs():
    q = deque()
    q.append([0,0])
    visited[0][0] = 1
    cnt = 0
    # 한번 while문 끝날 때마다 1시간 지난다.
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and visited[nx][ny]==0:
                if graph[nx][ny] == 0:
                    visited[nx][ny] = 1
                    # 치즈가 아닌 부분만 q에 넣어준다.
                    # 가장자리만 체크해주기위함
                    q.append([nx,ny])
                elif graph[nx][ny] == 1:
                    # !!!!!!!!!!!!!!!!!!!!!!!!이부분이 중요!!!!!!!!!!!!!!!!!!!!!!!!!!

                    # 가장자리 부분만 처리해주기때문에 만약에 공기와 접촉한 칸은 q에 넣어주지않는다.
                    # 넣게되면 안쪽 치즈까지 녹음 처리 되기 때문이다.
                    graph[nx][ny] = 0
                    visited[nx][ny] = 1
                    cnt += 1
    ans.append(cnt)
    return cnt

time = 0
while 1:
    time +=1
    # 특수한 경우이기 때문에 0,1 밖에 없긴하지만 visited 리스트를 하나 만들어준다.
    # 0을 1로 바꾸거나 1을 0으로 바꾸면 방문처리가 되지만, 그렇게되면 bfs특성상 다르게 구현이된다.
    visited = [[0]*m for _ in range(n)]
    cnt = bfs() 
    if cnt == 0:
        break
print(time-1)
print(ans[-2])