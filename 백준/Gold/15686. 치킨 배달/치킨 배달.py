from collections import deque
from itertools import combinations

# BFS로 최소 치킨 거리를 계산하는 함수
def bfs(city, chickens, m):
    n = len(city)
    CountOfHouse = 0

    # 집의 수를 세기
    for x in range(n):
        for y in range(n):
            if city[x][y] == 1:
                CountOfHouse += 1

    result = 2500 * 100  # 결과값 최대값으로 초기화

    # 치킨집의 경우의 수를 조합으로 생성
    for chicken in list(combinations(chickens, m)):
        # 치킨집 조합에 따른 도시 맵 초기화
        map_ = [x[:] for x in city]
        queue = deque([])
        distance = 0 # 치킨 거리 초기화
        count = 0

        # 선택된 치킨집을 큐에 추가하고 도시 맵에서 표시
        for x in chicken:
            map_[x[0]][x[1]] = 2
            queue.append([x[0], x[1]])

        # BFS 탐색
        while queue:
            x, y = queue.popleft()

            # 상하좌우 이동
            for dx, dy in [[1,0], [-1,0], [0,1], [0,-1]]:
                if 0<=x+dx<=n-1 and 0<=y+dy<=n-1:
                    if map_[x+dx][y+dy] == 1: # 집에 도착한 경우
                        queue.append([x+dx, y+dy])
                        map_[x+dx][y+dy] = map_[x][y] + 1
                        distance += map_[x+dx][y+dy] - 2 # 집에 도착할 경우 치킨 거리를 누적
                        count += 1

                    elif map_[x+dx][y+dy] == 0: # 빈 공간인 경우
                        queue.append([x+dx, y+dy])
                        map_[x+dx][y+dy] = map_[x][y] + 1
        
            # 모든 집을 방문했으면 종료
            if CountOfHouse == count:
                break

        # 현재 치킨집 조합에 대한 최소 치킨 거리를 저장
        result = min(result, distance)

    return result

# 문제 풀이 시작
n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]
house = []      # 집의 위치를 저장할 리스트
chickens = []   # 치킨집의 위치를 저장할 리스트

# 도시 맵을 순회하며 집과 치킨집의 위치를 파악
for x in range(n):
    for y in range(n):
        if city[x][y] == 1:  # 집인 경우
            house.append([x, y])
        if city[x][y] == 2:  # 치킨집인 경우
            chickens.append([x, y])
            city[x][y] = 0   # 해당 위치의 값을 0으로 초기화 (치킨집은 도시에서 제거)

# 최소 치킨 거리 계산 함수 호출
result = bfs(city, chickens, m)

# 결과 출력
print(result) # 최소 치킨 거리 출력





