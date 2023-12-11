# https://ddingmin00.tistory.com/entry/%EB%B0%B1%EC%A4%80%ED%8C%8C%EC%9D%B4%EC%8D%AC-3055%EB%B2%88-%ED%83%88%EC%B6%9C 참고

from collections import deque
import sys

# input
n, m = map(int, sys.stdin.readline().split())
grid = []
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

for i in range(n):
    grid.append(list(sys.stdin.readline().rstrip()))
    for j in range(m):
        if grid[i][j] == 'S':
            start = (i, j)  # 고슴도치의 시작 위치
            grid[i][j] = '.'  # 고슴도치의 위치를 빈 곳으로 변경
        elif grid[i][j] == 'D':
            end = (i, j)  # 비버의 굴 위치
            grid[i][j] = '.'  # 비버의 굴 위치를 빈 곳으로 변경

def bfs():
    global end
    ex, ey = end
    
    ans = 0
    q = deque()
    visited = [[0] * m for _ in range(n)]
    i, j = start
    q.append((i, j))
    visited[i][j] = 1
    
    while q:
        # 고슴도치의 이동
        for _ in range(len(q)):
            i, j = q.popleft()
            
            for k in range(4):
                x, y = i + dx[k], j + dy[k]
                if not(0 <= x < n and 0 <= y < m):
                    continue
                if visited[x][y] == 0 and grid[x][y] == '.':
                    # 도착 지점인지 확인
                    if x == ex and y == ey:
                        return ans + 1  # 최단 경로에 도달했을 때 시간 반환
                    
                    # 다음 물이 찰 예정인지 체크
                    flag = 1
                    for kk in range(4):
                        cx, cy = x + dx[kk], y + dy[kk]
                        if not(0 <= cx < n and 0 <= cy < m): continue
                        if grid[cx][cy] == '*': flag = 0
                    
                    if flag:
                        q.append((x, y))  # 다음 위치로 이동 가능하면 큐에 추가
                        visited[x][y] = 1  # 방문 표시
        
        # 물 확장
        water = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '*':
                    for k in range(4):
                        x, y = i + dx[k], j + dy[k]
                        if not(0 <= x < n and 0 <= y < m):
                            continue
                        # 도착지점은 물 번지지 않도록 예외 처리
                        if x == ex and y == ey:
                            continue
                        if grid[x][y] == '.':
                            water.append((x, y))
        
        for x, y in water:
            grid[x][y] = '*'  # 물이 번짐
        
        ans += 1  # 시간 증가
        
    return "KAKTUS"  # 비버의 굴에 도달할 수 없는 경우

print(bfs())