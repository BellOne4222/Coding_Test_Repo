# 1. 시간 초과 때문에 실패 : 리스트 내에서 움직여서 시간복잡도가 o(n^2) 
def solution(players, callings):
    for i in callings:
        a = players.index(i)
        b = (a-1)
        players[b], players[a] = players[a], players[b]
        
    result = []
    for j in players:
        result.append(j)
    return result

# 2. 딕셔너리 적용
def solution(players, callings):
    players_dict = {value: key for key, value in enumerate(players)}
    rank = {value:key for key,value in players_dict.items()}
    
    for calling in callings:
        a = players_dict[calling]  
        b = a - 1
        players[b], players[a] = players[a], players[b]  
    
    return players

# 3. 딕셔너리 사용해서 시간 복잡도를 줄이고, 등수 딕셔너리를 따로 만들어서 구현, 딕셔너리 내에서 조작해서 시간 복잡도 o(n+m)
def solution(players, callings):
    players_dict = {value: key for key, value in enumerate(players)} # {'mumu': 0, 'soe': 1, 'poe': 2, 'kai': 3, 'mine': 4}
    rank = {value:key for key,value in players_dict.items()} # {0: 'mumu', 1: 'soe', 2: 'poe', 3: 'kai', 4: 'mine'}

    for callee in callings:
        player_rank = players_dict[callee] # 부른 선수의 등수
        front_player_rank = player_rank - 1 # 부른 선수의 앞 선수 등수
        front_player = rank[front_player_rank] # 앞 선수 이름
        
        rank[player_rank] = front_player # 부른 선수를 앞 선수와 swap
        rank[front_player_rank] = callee # 앞 선수를 부른 선수와 swap
        
        players_dict[callee] = front_player_rank # 부른 선수의 등수를 앞 선수 등수와 swap
        players_dict[front_player] = player_rank # 앞 선수의 등수를 부른 사람 등수와 swap
    
    result = list(rank.values())
    return result
               
    
    
        
        
    
    