# cap, n, deliveries, pickups = 2,7,[1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]	
cap, n, deliveries, pickups = 4,	5,	[1, 0, 3, 1, 2],	[0, 3, 0, 4, 0]

deliveries = deliveries[::-1]  # 배열을 뒤집어서 뒤에서부터 처리하기 위해
pickups = pickups[::-1]        # 배열을 뒤집어서 뒤에서부터 처리하기 위해
answer = 0

have_to_deli = 0  # 현재 집까지 배달해야 하는 택배 상자의 개수
have_to_pick = 0  # 현재 집까지 수거해야 하는 빈 택배 상자의 개수

for i in range(n):
    have_to_deli += deliveries[i]  # 현재 집까지의 배달해야 하는 택배 상자의 개수 갱신
    have_to_pick += pickups[i]     # 현재 집까지의 수거해야 하는 빈 택배 상자의 개수 갱신

    while have_to_deli > 0 or have_to_pick > 0:  # 아직 배달이나 수거할 택배가 남아있을 경우
        have_to_deli -= cap  # 트럭에 실린 만큼 배달해야 하는 택배 개수 갱신
        have_to_pick -= cap  # 트럭에 실린 만큼 수거해야 하는 빈 택배 상자 개수 갱신
        answer += (n - i) * 2  # 현재 집에서 물류창고까지의 이동 거리를 더함

print(answer)
                    
                        
                    
                    
        
    
        
            
            

