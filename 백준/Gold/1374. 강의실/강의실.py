import sys
import heapq
n = int(sys.stdin.readline())
missions = [] # [[3, 2, 14], [1, 3, 8], [5, 6, 20], [8, 6, 27], [2, 7, 13], [4, 12, 18], [6, 15, 21], [7, 20, 25]]

room = 1

for i in range(n):
    mission = list(map(int, sys.stdin.readline().split()))
    missions.append(mission)

missions = sorted(missions, key=lambda x:(x[1],x[2]))

finish_time = []
heapq.heapify(finish_time)
heapq.heappush(finish_time, (missions[0][2],missions[0][1]))

for i in range(1,len(missions)):
    if finish_time[0][0] > missions[i][1]:
        heapq.heappush(finish_time, (missions[i][2],missions[i][1]))
    else:
        heapq.heappop(finish_time)
        heapq.heappush(finish_time, (missions[i][2],missions[i][1]))
    

print(len(finish_time))