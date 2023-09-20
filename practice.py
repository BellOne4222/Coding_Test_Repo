# 최소 치킨 거리를 구하기 위해 집의 개수, 위치, 치킨 집의 개수와 위치를 파악하고, 치킨 집에서의 집까지의 거리 합 중 최소의 거리를 구하여 치킨 거리로 반환

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

    result = 2500 * 100  # 결과값을 배열의 최대가 2500이므로 (50*50) * (50+50)으로 최대값을 정해서 result 생성

    # 치킨집의 경우의 수를 조합으로 생성(내장 함수 참고)
    for chicken in list(combinations(chicken_house, m)):
        # 치킨집 조합에 따른 새로운 도시 배열을 도시 배열을 복사해서 생성
        new_city = [x[:] for x in city]
        queue = deque([])
        distance = 0 # 치킨 거리 초기화
        count = 0 # 최소 거리를 위한 치킨 집 수

        # 선택된 치킨집을 큐에 추가하고 도시 배열에 추가
        for x in chicken:
            new_city[x[0]][x[1]] = 2
            queue.append([x[0], x[1]])

        # BFS 탐색
        while queue:
            x, y = queue.popleft()

            # 상하좌우 이동
            for dx, dy in [[1,0], [-1,0], [0,1], [0,-1]]:
                # 배열 안에서만 이동
                if 0<=x+dx<=n-1 and 0<=y+dy<=n-1:
                    if new_city[x+dx][y+dy] == 1: # 집에 도착한 경우
                        queue.append([x+dx, y+dy])
                        new_city[x+dx][y+dy] = new_city[x][y] + 1
                        distance += new_city[x+dx][y+dy] - 2 # 집일 경우의 치킨 거리 누적을 위해서 치킨 집과 집의 좌표를 빼서 -2 처리
                        count += 1  # 집 방문 했으니까 변수 += 1

                    elif new_city[x+dx][y+dy] == 0: # 빈 공간인 경우
                        queue.append([x+dx, y+dy])
                        new_city[x+dx][y+dy] = new_city[x][y] + 1
        
            # 모든 집을 방문했으면 종료
            if house_cnt == count:
                break

        # 현재 치킨집 조합에 대한 최소 치킨 거리를 저장
        result = min(result, distance)

    return result


n, m = map(int, input().split())

city = [list(map(int, input().split())) for _ in range(n)] # 도시 배열 받아오기
house = []      # 집의 위치를 저장할 리스트
chicken_house = []   # 치킨집의 위치를 저장할 리스트

# 도시 맵을 순회하며 집과 치킨집의 위치를 파악
for x in range(n):
    for y in range(n):
        if city[x][y] == 1:  # 집인 경우
            house.append([x, y])
        if city[x][y] == 2:  # 치킨집인 경우
            chicken_house.append([x, y])
            city[x][y] = 0   # 치킨집을 도시에서 제거하기 위해 0으로 초기화

# 최소 치킨 거리 계산 하기 위한 bfs 호출
result = bfs(city, chicken_house, m)


print(result) # 최소 치킨 거리 출력