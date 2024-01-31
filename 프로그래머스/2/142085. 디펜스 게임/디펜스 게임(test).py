# 출처: https://magentino.tistory.com/51 [마젠티노 IT개발스토리:티스토리]

import heapq

n,	k,	enemy = 7,	3,	[4, 2, 4, 5, 3, 3, 1]

round = len(enemy)
if k >= round :
    round = round
else:
    q = []
    
    for i in range(round) :
        heapq.heappush(q, enemy[i])
        if len(q) > k :
            last = heapq.heappop(q)
            if last > n :
                break
            n -= last

    
print(i)