# 문제를 못풀어서 gpt, 블로그 참고하고 수정하고 공부했습니다...


maxScore = 0       # 가장 큰 점수 차이
maxList = []       # 가장 큰 점수 차이를 낸 배열 

# dfs(index, score, n, apeach): 이 함수는 DFS(Depth-First Search) 방식을 사용하여 가능한 모든 경우의 수를 탐색합니다. index는 현재까지 확인한 점수의 인덱스, score는 라이언의 점수를 나타내는 배열, n은 남은 공격 횟수, 
# apeach는 어피치의 각 점수에 해당하는 배열입니다. 이 함수는 횟수가 0일 때 calScore() 함수를 호출하고 반환합니다.

def dfs(index, score, n, apeach) : 
    if n == 0 : # 남은 공격 횟수 n이 0일 때, 즉 모든 공격을 사용했을 때에는 라이언의 점수 조합이 확정되었으므로 calScore() 함수를 호출하여 라이언과 어피치의 점수를 계산합니다. 
        # 이후에는 더 이상 점수를 변경할 수 없으므로 return으로 함수를 종료합니다.
        calScore(score, apeach)
        return
    
    if index == 11: 
        return    # 0~10까지의 점수만 존재
    
    sc = apeach[index]         # 어피치가 (index)점을 맞힌 횟수, apeach 배열에서 index에 해당하는 점수를 맞힌 횟수를 가져옵니다.
    for i in range(sc+2):    # 0부터 (index)+1까지 맞히는 경우만 고려 ,i는 현재 점수를 맞힐 횟수를 나타냅니다.
        if n >= i:           # n보다 크면 안되니까 고려, 남은 공격 횟수 n이 i보다 크거나 같은 경우에만 해당 점수를 선택할 수 있습니다. i는 0부터 sc + 1까지의 값을 가지므로, 
            # n보다 큰 값은 더 이상 해당 점수를 선택할 수 없음을 의미합니다.
            score[index] = i # 해당 점수를 선택
            dfs(index+1, score, n-i, apeach) #  다음 인덱스인 index + 1을 선택하도록 재귀 호출합니다. 이때, n은 i 만큼 감소하며, 선택된 점수를 반영
            score[index] = 0 # 재귀 호출이 끝난 후에는 해당 인덱스의 값을 초기화하여 이전 상태로 돌아갑니다. 이후 반복문을 통해 다른 점수를 선택하는 경우의 수를 확인
    
# calScore(ryan, apeach): 이 함수는 라이언과 어피치의 점수를 계산하여 최대 점수 차이를 구하고, 그에 해당하는 점수 배열을 maxList에 저장합니다. ryan과 apeach는 각각 라이언과 어피치의 점수 배열을 나타냅니다. 
# 이 함수에서는 라이언과 어피치가 0점이 아닌 점수를 맞혔을 때에만 점수를 계산합니다. 라이언의 점수가 어피치보다 높을 경우 라이언은 해당 점수에 대해 (10 - i)만큼의 점수를 획득하고, 어피치는 점수를 획득하지 못합니다. 
# 이후 최대 점수 차이를 계산하여 maxScore와 maxList를 갱신합니다.

#  n == 0일 때, 더 이상 남은 공격 횟수가 없다는 의미이므로 현재까지 결정한 라이언의 점수를 기반으로 calScore() 함수를 호출\
def calScore(ryan, apeach):    # 점수 계산 함수
    global maxScore, maxList
    rScore = 0    # 라이언 점수
    aScore = 0    # 어피치 점수
    
    for i in range(11):
        if ryan[i] == 0 and apeach[i] == 0:
            continue    # 둘다 0이면 0 점으로 continue
        
        if ryan[i] > apeach[i]:
            rScore += (10-i)    # 라이언이 더 많이 맞췄으면 점수획득
        else:
            aScore += (10-i)    # 아니면 어피치 점수획득
        
    if rScore > aScore :    # 라이언 점수가 더 높을 때만 고려
        diff = rScore - aScore # 점수 차이 = 라이언 점수 - 어피치 점수
        if diff > maxScore:    # 최대값 갱신
            maxScore = diff
            maxList = list(ryan)
            
        elif diff == maxScore: # 최대값이 같을 경우
            for i in range(11):    
                if ryan[-i] > maxList[-i]: # 낮은 점수를 많이 맞은 경우가 선택
                    maxList = list(ryan)
                    break
                elif ryan[-i] < maxList[-i]:
                    break
                    
# solution(n, info): 이 함수는 주어진 입력에 대해 문제를 해결합니다. n은 남은 공격 횟수를 나타내고, info는 어피치가 각 점수에 대해 맞힌 횟수를 나타내는 배열입니다. 
# 이 함수에서는 임시로 0으로 초기화된 배열 target을 생성한 후, dfs() 함수를 호출하여 가능한 모든 경우의 수를 탐색합니다. 마지막으로 maxList의 길이가 0인 경우 -1을 반환하고, 그렇지 않은 경우 maxList를 반환합니다.
def solution(n, info):
    target = [0 for i in range(11)]
    dfs(0, target, n, info)  
    
    if len(maxList) == 0: 
        return [-1]
    else: 
        return maxList







