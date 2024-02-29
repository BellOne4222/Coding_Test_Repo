import sys
from itertools import combinations
from collections import deque

n,m = map(int, sys.stdin.readline().split())

graph = [[]*(n+1) for _ in range(n+1)] # # [[], [3], [3, 4, 5], [1, 2], [2], [2]]

for _ in range(m):
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)
    graph[start].sort()
    graph[end].append(start)
    graph[end].sort()

nums = [i for i in range(1,n+1)] 
chicken_houses = list(combinations(nums,2)) # [(1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5)]

per_distances = [] 
# [[0, 0, 0, 1, 1, 1], [0, 0, 1, 0, 2, 2], [0, 0, 1, 1, 0, 2], [0, 0, 1, 1, 2, 0], [0, 1, 0, 0, 1, 1], [0, 2, 0, 1, 0, 1], [0, 2, 0, 1, 1, 0], [0, 1, 1, 0, 0, 2], [0, 1, 1, 0, 2, 0], [0, 3, 1, 2, 0, 0]]


for chicken_house in chicken_houses:
    visited = [False] * (n+1)
    queue = deque()
    candidation_1, candidation_2 = chicken_house
    queue.append([candidation_1,0])
    queue.append([candidation_2,0])
    visited[candidation_1] = True
    visited[candidation_2] = True
    distances = [0 for _ in range(n+1)]
    while queue:
        cur_chicken_house, depth = queue.popleft()
        
        if distances[cur_chicken_house] == 0:
            distances[cur_chicken_house] = depth
        
        for next_chicken_house in graph[cur_chicken_house]:
            if not visited[next_chicken_house]:
                visited[next_chicken_house] = True
                queue.append([next_chicken_house,depth+1])
    
    per_distances.append(distances)

arr = list(zip(per_distances, chicken_houses))
arr.sort(key=lambda x: (sum(x[0]),x[1][0],x[1][1]))
# [([0, 0, 0, 1, 1, 1], (1, 2)), ([0, 1, 0, 0, 1, 1], (2, 3)), ([0, 0, 1, 1, 0, 2], (1, 4)), 
# ([0, 0, 1, 1, 2, 0], (1, 5)), ([0, 2, 0, 1, 0, 1], (2, 4)), ([0, 2, 0, 1, 1, 0], (2, 5)), 
# ([0, 1, 1, 0, 0, 2], (3, 4)), ([0, 1, 1, 0, 2, 0], (3, 5)), ([0, 0, 1, 0, 2, 2], (1, 3)), 
# ([0, 3, 1, 2, 0, 0], (4, 5))]

print("{} {} {}".format(arr[0][1][0], arr[0][1][1], sum(arr[0][0])*2))

