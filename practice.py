import heapq
import sys

input = sys.stdin.readline()

arr = []

heapq.heapify(arr) # arr을 heapq로 변경

n = int(input())

for _ in range(n):
    x = int(input())  
    # x가 0이 아니면 heappush
    if x != 0: 
        heapq.heappush(arr,(abs(x),x)) # 우선 순위, 값형식의 튜플로 저장
    # x가 0이면 heappop
    else:
        if arr:
            print(heapq.heappop(arr)[1])
        else:
            print(0)