# sys 모듈을 임포트하여 표준 입력에서 데이터를 읽을 수 있게 합니다.
import sys

# heapq 모듈을 임포트하여 최소 힙을 사용할 수 있게 합니다.
import heapq

# n에 정수를 입력받습니다. 이 값은 미션의 개수를 나타냅니다.
n = int(sys.stdin.readline())

# 미션들을 저장할 리스트를 초기화합니다.
missions = []

# 각 미션에 대한 정보를 입력받아 missions 리스트에 추가합니다.
# 미션은 [시작 시간, 종료 시간, 보상]의 형태로 저장됩니다.
for i in range(n):
    mission = list(map(int, sys.stdin.readline().split()))
    missions.append(mission)

# missions 리스트를 종료 시간(mission[1])과 보상(mission[2])을 기준으로 정렬합니다.
# 종료 시간이 같을 경우 보상이 높은 순서로 정렬됩니다.
missions = sorted(missions, key=lambda x: (x[1], x[2]))


# 미션의 종료 시간을 저장할 우선순위 큐(힙)를 초기화합니다.
finish_time = []
heapq.heapify(finish_time)

# 첫 번째 미션의 종료 시간과 시작 시간을 힙에 추가합니다.
heapq.heappush(finish_time, (missions[0][2], missions[0][1]))

# 모든 미션에 대해 반복합니다.
for i in range(1, len(missions)):
    # 가장 일찍 끝나는 미션의 종료 시간(finish_time[0][0])과 현재 미션의 시작 시간(missions[i][1])을 비교합니다.
    if finish_time[0][0] > missions[i][1]:
        # 만약 현재 미션을 수행할 수 없다면, 현재 미션의 종료 시간과 시작 시간을 힙에 추가합니다.
        heapq.heappush(finish_time, (missions[i][2], missions[i][1]))
    else:
        # 그렇지 않으면, 가장 일찍 끝나는 미션을 빼고 현재 미션을 추가합니다.
        heapq.heappop(finish_time)
        heapq.heappush(finish_time, (missions[i][2], missions[i][1]))

# 모든 미션을 수행하는 데 필요한 방의 최소 개수는 finish_time 큐의 길이입니다.
print(len(finish_time))