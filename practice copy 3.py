cap,	n,	deliveries,	pickups = 2,7,[1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]	

total_distance = 0
    
    
while True:
    cur_cap = 0
    delivery_cnt = False
    pickup_cnt = False
    delivery = 0
    pickup = 0
    delivery_distance = 0
    pickup_distance = 0
    last_delivery = 0
    
    for i in reversed(range(n)):
        if deliveries[i] != 0:
            if cur_cap + deliveries[i] <= cap:
                cur_cap += deliveries[i]
                delivery += deliveries[i]
                deliveries[i] = 0
                
                if not delivery_cnt:
                    delivery_cnt = True
                    delivery_distance += i+1
                    last_delivery = i+1
            else:
                break
    
    cur_cap = 0
     
        
    for j in reversed(range(n)):
        if pickups[j] != 0:
            if cur_cap + pickups[j] <= cap:
                cur_cap += pickups[j]
                pickups[j] = 0
                if not pickup_cnt:
                    pickup_cnt = True
                    if last_delivery != 0:
                        pickup_distance += last_delivery
                    else:
                        pickup_distance += j+1
                        
            else:
                break
        
    total_distance += delivery_distance
    total_distance += pickup_distance
        
    if all(element == 0 for element in deliveries) and all(element == 0 for element in pickups):
        break

print(total_distance)