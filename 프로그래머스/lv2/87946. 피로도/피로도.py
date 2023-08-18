# 유저가 탐험할수 있는 최대 던전 수를 return 하도록을 보고 dp 보다는 dfs로 모든 경우의 수를 보고 거기에서 가장 깊이 탐험한(탐험을 가장 많이 한) 경우에서의 탐험 횟수를 반환하는 방식을 생각해서 구현

result = 0

def dfs(k, dungeons, adventure, adventured):
    global result
    # 유저가 탐험할수 있는 최대 던전 수를 return
    result = max(result, adventure)
    
    for i in range(len(dungeons)):
        if k >= dungeons[i][0] and adventured[i] == 0: # 현재 피로도가 탐험 할 던전의 최소 피로도 보다 크거나 같고, 아직 탐험하지 않았다면
            adventured[i] = 1 # 탐험 처리
            dfs(k-dungeons[i][1], dungeons, adventure+1, adventured) # 현재 피로도에서 탐험한 던전의 필요 피로도만큼 빼주고, 탐험한 횟수 1 추가 해서 dfs 다시 호출
            adventured[i] = 0 # 모든 경우의 수를 구하기 위해서 탐험한 곳을 안한 곳으로 재설정해서 탐색
            
            
def solution(k, dungeons):
    adventured = [0] * len(dungeons) # 탐험 할 지역 생성
    dfs(k, dungeons, 0, adventured) # 현재 피로도, 피로도 배열, 탐험 횟수, 탐험 할 지역
    return result

print(solution(80, [[80,20],[50,40],[30,10]]))
        