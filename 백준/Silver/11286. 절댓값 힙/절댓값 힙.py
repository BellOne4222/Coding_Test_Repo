import heapq as hp
import sys

input = sys.stdin.readline
pq = []
for _ in range(int(input())):
    x = int(input())
    if x:
        hp.heappush(pq,(abs(x), x))
    else:
        if pq:
            print(hp.heappop(pq)[1])
        else:
            print(0)