# cap, n, deliveries, pickups = 2,7,[1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]	
cap, n, deliveries, pickups = 4,	5,	[1, 0, 3, 1, 2],	[0, 3, 0, 4, 0]

total_distance = 0

while True:
    cur_cap = cap
    delivery_distance = 0
    delivery_chk = False
    last_delivery = 0
    pickup_distance = 0
    pickup_chk = False
    
    # 배달
    if not all(element == 0 for element in deliveries):
        for i in reversed(range(n)):
        # 배달 할 물건이 있을 떄
            if deliveries[i] != 0:
                # 집에 배달 할 수 있는 택배의 수를 모두 배달 할 수 있는 경우
                if cur_cap - deliveries[i] >= 0:
                    cur_cap -= deliveries[i] # 택배 모두 배송
                    if not delivery_chk: # 제일 끝 배달한 집 주소 저장
                        delivery_chk = True
                        delivery_distance += i+1
                        last_delivery = i+1
                    deliveries[i] = 0
                    
                
                # 집에 배달 할 수 있는 택배의 수를 모두 배달 할 수 없는 경우
                else:
                    if cur_cap != 0:
                        deliveries[i] = deliveries[i] - cur_cap # 부분 배달 처리
                        break
                # 트럭이 가득차면 배달 종료
                if cur_cap == 0:
                    break
        
    
        
    if not all(element == 0 for element in pickups):
        # 수거
        for j in reversed(range(n)):
            # 수거 할 물건이 있을 때
            if pickups[j] != 0:
                # 집에 있는 박스를 모두 수거 할 수 있는 경우
                if cur_cap + pickups[j] <= cap:
                    cur_cap += pickups[j] # 수거
                    pickups[j] = 0
                    
                    if not pickup_chk:
                        pickup_chk = True
                        last_pickup = j+1 
                    
                    # 배송한 가장 끝집부터 수거 하므로 배송한 가장 마지막 지점부터 수거 거리 계산
                    if last_delivery != 0:
                        pickup_distance += last_delivery
                    # 배송을 안하고 수거만 한 경우
                    else:
                        pickup_distance += last_pickup
                # 부분 수거
                else:
                    if cur_cap < cap:
                        pickups[j] = pickups[j] - (cap - cur_cap)
                        
                
    
    total_distance += delivery_distance
    total_distance += pickup_distance
        
    if all(element == 0 for element in deliveries) and all(element == 0 for element in pickups):
        break

print(total_distance)
                    
                        
                    
                    
        
    
        
            
            

