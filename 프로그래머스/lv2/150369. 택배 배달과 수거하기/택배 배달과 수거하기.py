def solution(cap, n, deliveries, pickups):
    move = 0 # 움직인 거리
    
    # 배달, 수거 할 곳이 없어질때 까지 반복
    while deliveries or pickups:
        # 가장 멀리 있는 곳이 갈 필요가 없어지면(0이면), 없애기
        while deliveries and deliveries[-1] == 0:
            del deliveries[-1]
        while pickups and pickups[-1] == 0:
            del pickups[-1]
        # 배달하러 가는것, 수거하러 다시 오는것 해서 거리 2배처리하고, 가장 먼 곳을 갔다오기 때문에 배열의 길이 중 가장 긴 배열의 길이에 2배 한거를 move에 더하기
        move += 2 * max(len(deliveries),len(pickups))
        
        
        # 배달 배열을 뒤집어서 반복문 돌려서 가장 먼 곳 부터 방문
        can_deliver = cap
        for i in reversed(range(len(deliveries))):
            # 배달 간 곳에 배달할 양이 가지고 온것 보다 많으면 배달할 양에서 가지고 온 것만큼 빼고, 
            if can_deliver < deliveries[i]:
                deliveries[i] -= can_deliver
                break
            # 배달 간 곳에 배달할 양이 가지고 온것 보다 적으면 가지고 온것에서 배달할 양을 빼고 배달 간 곳을 0으로 바꿔서 처리 
            else:
                can_deliver -= deliveries[i]
                deliveries[i] = 0
        
        can_pick = cap
        for j in reversed(range(len(pickups))):
            if can_pick < pickups[j]:
                pickups[j] -= can_pick
                break
            else:
                can_pick -= pickups[j]
                pickups[j] = 0
    
    
    return move
                
        
        
    