import heapq

n,	k,	enemy = 7,	3,	[4, 2, 4, 5, 3, 3, 1]

stage = len(enemy)
if k >= stage :
    stage = stage
else:
    q = []
    
    for i in range(stage) :
        heapq.heappush(q, enemy[i])
        if len(q) > k :
            last = heapq.heappop(q)
            if last > n :
                break
            n -= last
# 출처: https://magentino.tistory.com/51 [마젠티노 IT개발스토리:티스토리]
    
print(i)