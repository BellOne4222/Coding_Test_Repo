import sys
from collections import deque
dx = [0, 0, 1, -1] # 동서남북
dy = [1, -1, 0, 0] # 동서남북
input = sys.stdin.readline
n = int(input())
arr = [list(input().rstrip()) for _ in range(n)]
cnt = [[1e9]*n for _ in range(n)] # 흰 방으로 바꾼 횟수
queue = deque()
queue.append((0, 0))
cnt[0][0]=0
while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<n and 0<=ny<n:
            if arr[nx][ny]=='1' and cnt[nx][ny] > cnt[x][y]:
                cnt[nx][ny] = cnt[x][y]
                queue.append((nx, ny))
            elif arr[nx][ny]=='0' and cnt[nx][ny] > cnt[x][y]: 
                cnt[nx][ny] = cnt[x][y]+1
                queue.append((nx, ny))

print(cnt[n-1][n-1])