result = 10 ** 6


def dfs(picks, minerals, fatigability):
    global result

    if sum(picks) == 0 or not minerals: # 곡괭이가 없거나 캘 광물이 없을 때, 피로도 반환
        result = min(fatigability, result)
        return

    for i in range(len(picks)):
        fatigue = 0
        if picks[i] >= 1:
            picks[i] -= 1
            mined = minerals[:5]
            if i == 0: # 다이아 곡괭이 일때
                fatigue += len(mined)
            elif i == 1: # 철 곡괭이 일때
                for mineral in mined:
                    if mineral == "diamond":
                        fatigue += 5
                    else:
                        fatigue += 1
            elif i == 2: # 돌 곡괭이 일때
                for mineral in mined:
                    if mineral == "diamond":
                        fatigue += 25
                    elif mineral == "iron":
                        fatigue += 5
                    else:
                        fatigue += 1
            dfs(picks, minerals[5:], fatigability + fatigue) # 광물 배열에서 5개 캤으므로 5부터 잘라서 다시 dfs 호출
            picks[i] += 1 # 곡괭이를 하나 썼고 다음 광물 캘때의 곡괭이 조합에서 다시 사용할 수 있게 1개 다시 추가


def solution(picks, minerals):
    dfs(picks,minerals,0)
    return result