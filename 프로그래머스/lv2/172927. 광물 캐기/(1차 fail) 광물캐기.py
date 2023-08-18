from collections import deque

def solution(picks, minerals):
    mine = deque() # ['dia', 'iron', 'iron', 'iron', 'stone', 'stone']
    pick = ["dia", "iron", "stone"]
    k = -1
    for i in picks:
        k += 1
        for j in range(i):
            mine.append(pick[k])
    minerals = deque(minerals)
    fatigability = 0
    mine_pick = ''
    for l in range(len(mine)):
        while mine or minerals:
            if len(mine) == 0:
                break
            mine_pick = mine[l]
            mine.popleft()
            for m in range(5):
                if len(minerals) == 0:
                    break
                if mine_pick == "dia":
                    minerals.popleft()
                    fatigability += 1
                elif mine_pick == "iron":
                    if minerals[0] == 'diamond':
                        fatigability += 5
                        minerals.popleft()
                    else:
                        fatigability += 1
                        minerals.popleft()
                else:
                    if minerals[0] == "diamond":
                        fatigability += 25
                        minerals.popleft()
                    elif minerals[0] == "iron":
                        fatigability += 5
                        minerals.popleft()
                    else:
                        fatigability += 1
                        minerals.popleft()
    return fatigability

print(solution([1, 3, 2], ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]))