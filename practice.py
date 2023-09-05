n = int(input())

houses = []
graph = []
for _ in range(n):
    graph.append(list(map(int,input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]    
    
def dfs(x,y):
    
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    
    if graph[x][y] == 1:
        global house_cnt
        house_cnt += 1
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx,ny)
        return True
    return False
    

house_cnt = 0
village_cnt = 0


for j in range(n):
    for k in range(n):
        if dfs(j,k) == True:
            houses.append(house_cnt)
            village_cnt += 1
            houses_cnt = 0

# 오름차순 정렬
houses.sort()
print(village_cnt)
for l in range(len(houses)):
    print(houses[l])