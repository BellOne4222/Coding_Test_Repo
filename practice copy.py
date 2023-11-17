import sys

inputs = list(map(int,sys.stdin.readline().split()))

n = inputs[0]

answer = 0

p = []

for i in range(1,5):
    p.append(inputs[i] * 0.01)

visited = [[False] * 29 for _ in range(29)] # n은 최대 14이므로

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(x, y, depth, pstack):
    global answer
    visited[x][y] = True # 방문 처리
    for i in range(4): # 동서남북 방문
        if not visited[x + dx[i]][y + dy[i]]: # 방문한 곳이 아니면
            if depth >= n: 
                answer += pstack * p[i]
            else: # 재귀 호출
                dfs(x + dx[i], y + dy[i], depth + 1, pstack * p[i])

    visited[x][y] = False

dfs(0,0,1,1)

print(answer)