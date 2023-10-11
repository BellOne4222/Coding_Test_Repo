import heapq
import sys

arr = []

heapq.heapify(arr) # arr을 heapq로 변경

n = int(sys.stdin.readline())

for _ in range(n):
    x = int(sys.stdin.readline())  
    # x가 0이 아니면 heappush
    if x != 0: 
        heapq.heappush(arr,(abs(x),x)) # 우선 순위, 값형식의 튜플로 저장
    # x가 0이면 heappop
    else:
        if arr:
            print(heapq.heappop(arr)[1])
        else:
            print(0)