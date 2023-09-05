# dfs

n = int(input())
graph = []
houses = [] # 집 개수를 받을 배열


for i in range(n):
    graph.append(list(map(int,input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]    
    
def dfs(x,y):
    # 범위 벗어나면 False
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    
    # 그래프의 칸이 1이면 집이 있는 곳이므로 집 개수 +=1
    if graph[x][y] == 1:
        global house_cnt
        house_cnt += 1
        # 세었으면 방문 처리
        graph[x][y] = 0

        # 상하좌우로 dfs 실행해서 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx,ny)
        return True
    return False
    

house_cnt = 0 # 집 개수
village_cnt = 0 # 마을 개수

# True이면 집 개수 배열에 추가하고 마을 개수 += 1 하고 집 개수 초기화
for j in range(n):
    for k in range(n):
        if dfs(j,k) == True:
            houses.append(house_cnt)
            village_cnt += 1
            house_cnt = 0

# 오름차순 정렬
houses.sort()
print(village_cnt)
for l in range(len(houses)):
    print(houses[l])