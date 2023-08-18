# 먼저 주어진 land과 같은 shape의 highest_land라는 리스트를 생성합니다. 이때 모든 값은 0으로 초기화합니다. 

# highest_land의 두 번째 줄부터, 각 위치에 도달할 때까지의 최댓값을 highest_land에 저장합니다. 이때 연속해서 같은 열은 방문할 수 없게 해줍니다. 

# cf. highest_land의 첫 번째 줄에선 아직까지 더해온 값이 없어 그대로 0이므로 고려하지 않아도 됩니다. 

# highest_land의 마지막 줄에 다다를 때까지 이를 반복하고, 마지막 줄에 도달하면 while문을 종료합니다.

 

# 여기까지 실행하면 highest_land의 마지막 줄엔 land의 마지막 줄의 각 위치에 도달할 때까지의 최댓값이 저장되어 있습니다. 이 값들을 각각 land의 위치에 해당하는 값과 더해주면, 각 위치에서 가능한 최종적인 합의 최댓값을 구할 수 있습니다. 이 리스트의 최댓값을 반환하면 정답을 얻을 수 있습니다. 

def solution(land):
    N = len(land)
    highest_land = [[0]*4 for i in range(N)] # 첫 번째 줄
    depth = 1 # 두 번째 줄부터 시작

    # highest_land를 각 위치에서 가능한 최댓값으로 채우기 
    while depth < N: # highest_land의 마지막 줄에 다다를 때까지 이를 반복하고, 마지막 줄에 도달하면 while문을 종료
        for idx, val in enumerate(land[depth]):
            # 연속해서 같은 열은 방문 할 수 없게 조건문 걸어서 가능한 idx 생성
            possible_idx = [i for i in [0,1,2,3] if i != idx]

            max_val = 0
            for i in possible_idx:
                val = highest_land[depth-1][i] + land[depth-1][i]
                if max_val < val:
                    max_val = val 

            highest_land[depth][idx] = max_val

        depth += 1

    # highest_land의 마지막 줄의 값들을 각각 해당하는 값과 더해 최댓값을 반환 
    return max([a+b for a,b in zip(highest_land[-1], land[-1])])