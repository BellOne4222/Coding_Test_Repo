import sys
from collections import deque
from itertools import combinations

def bfs(city, chickens, m):
    n = len(city)
    CountOfHouse = 0

    for x in range(n):
        for y in range(n):
            if city[x][y] == 1:
                CountOfHouse += 1

    result = 2500 * 100  # 결과값 최대값으로 초기화

    for chicken in list(combinations(chickens, m)): # 치킨집의 경우의 수
        map_ = [x[:] for x in city]
        queue = deque([])
        distance = 0 # 치킨거리 초기화
        count = 0

        for x in chicken: # 치킨집의 위치 큐에 저장
            map_[x[0]][x[1]] = 2
            queue.append([x[0], x[1]])

        # BFS 탐색
        while queue:
            x, y = queue.popleft()

            for dx, dy in [[1,0], [-1,0], [0,1], [0,-1]]:
                if 0<=x+dx<=n-1 and 0<=y+dy<=n-1:
                    if map_[x+dx][y+dy] == 1:
                        queue.append([x+dx, y+dy])
                        map_[x+dx][y+dy] = map_[x][y] + 1
                        distance += map_[x+dx][y+dy] - 2 # 집에 도착할 경우 치킨 거리를 누적
                        count += 1

                    elif map_[x+dx][y+dy] == 0:
                        queue.append([x+dx, y+dy])
                        map_[x+dx][y+dy] = map_[x][y] + 1

            if CountOfHouse == count:
                break
        result = min(result, distance) # 매 경우의 수마다 최소 치킨거리 저장

    return result

# 문제 풀이
n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]
house = []
chickens = []

for x in range(n):
    for y in range(n):
        if city[x][y] == 1:
            house.append([x, y])
        if city[x][y] == 2:
            chickens.append([x, y])
            city[x][y] = 0

result = bfs(city, chickens, m)
print(result) # 최소 치킨 거리 출력