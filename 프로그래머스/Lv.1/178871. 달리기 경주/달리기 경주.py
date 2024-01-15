def solution(players, callings):
    
    idxs = [i for i in range(len(players))]
    
    idx_dictionary = {k:v for k, v in zip(players, idxs)}
    # idx_dictionary = {player: i for i, player in enumerate(players)} # 선수: 등수
    
    for j in callings:
        
        
        idx = idx_dictionary[j] # 호명된 선수의 현재 등수
        
        idx_dictionary[j] -= 1 # 하나 앞 등수로 바꿔줌 -1
        
        idx_dictionary[players[idx-1]] += 1 # 앞에 위치했던 선수의 등수 +1
        
        players[idx-1], players[idx] = players[idx], players[idx-1] # 위치 변경
    return players