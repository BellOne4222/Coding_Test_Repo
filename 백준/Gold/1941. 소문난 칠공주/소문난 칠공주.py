import sys
from collections import deque

def bfs(x, y): #  BFS를 통해 특정 위치에서 시작하여 인접한 학생들의 수가 7명인지 확인
    # BFS 탐색 함수
    queue = deque()
    bfs_visited = [[0]*5 for _ in range(5)]  # 방문 여부를 저장하는 배열
    queue.append([x, y])
    bfs_visited[x][y] = 1
    cnt = 1  # 탐색한 노드 수를 카운트
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    while queue:
        cur_x, cur_y = queue.popleft()
        
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            
            if 0 <= nx < 5 and 0 <= ny < 5:
                if bfs_visited[nx][ny] == 0:
                    if visited[nx][ny] == 1:
                        queue.append([nx, ny])
                        bfs_visited[nx][ny] = 1
                        cnt += 1
    
    return cnt == 7  # 인접한 학생들의 수가 7명인지 확인

def check(): # '소문난 칠공주'를 결성할 수 있는지 확인하는 함수로, 모든 학생들을 돌며 'S'로 표시된 학생을 출발점으로 하여 bfs()를 호출
    # '소문난 칠공주'를 결성할 수 있는지 확인하는 함수
    for i in range(5):
        for j in range(5):
            if visited[i][j] == 1:
                if bfs(i, j):  # BFS로 인접한 학생들의 수가 7명인지 확인
                    return True
    return False

def dfs(cnt, w_cnt, s_cnt): # 재귀적으로 모든 경우의 수를 탐색하며, 'S'의 개수가 4 이상이고, '소문난 칠공주'의 조건을 만족하는 경우를 탐색
    # DFS를 통해 가능한 모든 조합을 탐색하는 함수
    global princess
    if w_cnt > 7:  # 가지치기(학생 수가 7명 초과시 종료)
        return
    
    if cnt == 25:
        if w_cnt == 7 and s_cnt >= 4:  # 그룹 인원이 7명이고 'S'의 수가 4 이상일 때
            if check():  # '소문난 칠공주'를 결성할 수 있는지 확인
                princess += 1
        
        return

    visited[cnt//5][cnt%5] = 1  # 포함하는 경우
    dfs(cnt+1, w_cnt+1, s_cnt + int(graph[cnt//5][cnt%5] == 'S'))
    visited[cnt//5][cnt%5] = 0  # 원상복구(백트래킹)
    dfs(cnt+1, w_cnt, s_cnt)  # 포함하지 않는 경우
    
# 입력
graph = [list(sys.stdin.readline().rstrip()) for _ in range(5)]
princess = 0
visited = [[0]*5 for _ in range(5)]
dfs(0, 0, 0)  # DFS 탐색
print(princess)  # 결과 출력
