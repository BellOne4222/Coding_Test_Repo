from collections import deque
from itertools import combinations

# BFS로 최소 치킨 거리를 계산하는 함수
def bfs(city, chicken_house, m):
    n = len(city)
    house_cnt = 0

    # 집의 수를 세기
    for x in range(n):
        for y in range(n):
            if city[x][y] == 1:
                house_cnt += 1

    result = 2500 * 100  # 결과값 최대값으로 초기화

    # 치킨집의 경우의 수를 내장함수 사용해서 조합으로 생성
    for chicken in list(combinations(chicken_house, m)):
        # 치킨집 조합에 따른 도시 배열 초기화
        new_city = [x[:] for x in city]
        queue = deque([])
        distance = 0 # 치킨 거리 초기화
        count = 0 # 방문한 집 개수 받을 변수

        # 선택된 치킨집을 큐에 추가하고 도시 맵에서 표시
        for x in chicken:
            new_city[x[0]][x[1]] = 2
            queue.append([x[0], x[1]])

        # BFS 탐색
        while queue:
            x, y = queue.popleft()

            # 상하좌우 이동
            for dx, dy in [[1,0], [-1,0], [0,1], [0,-1]]:
                if 0<=x+dx<=n-1 and 0<=y+dy<=n-1:
                    if new_city[x+dx][y+dy] == 1: # 집에 도착한 경우
                        queue.append([x+dx, y+dy])
                        new_city[x+dx][y+dy] = new_city[x][y] + 1
                        distance += new_city[x+dx][y+dy] - 2 # 집에 도착할 경우 치킨 거리를 누적하기 위해서 집과 치킨집 사이의 거리이므로 각 좌표를 빼기 위해 -2 처리
                        count += 1

                    elif new_city[x+dx][y+dy] == 0: # 빈 공간인 경우
                        queue.append([x+dx, y+dy])
                        new_city[x+dx][y+dy] = new_city[x][y] + 1
        
            # 모든 집을 방문했으면 종료
            if house_cnt == count:
                break

        # 현재 치킨집 조합에 대한 최소 치킨 거리를 result에 저장
        result = min(result, distance)

    return result


n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]
house = []      # 집의 위치를 저장할 리스트
chicken_house = []   # 치킨집의 위치를 저장할 리스트

# 도시 배열의 집과 치킨집의 위치를 파악
for x in range(n):
    for y in range(n):
        if city[x][y] == 1:  # 집인 경우
            house.append([x, y])
        if city[x][y] == 2:  # 치킨집인 경우
            chicken_house.append([x, y])
            city[x][y] = 0   # 치킨집에서 도시까지의 거리를 알기 위해 치킨집을 도시 배열에 0으로 초기화

# 최소 치킨 거리 계산을 하기 위해 BFS 호출
result = bfs(city, chicken_house, m)

print(result) # 최소 치킨 거리 출력