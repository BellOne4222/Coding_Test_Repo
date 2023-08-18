import sys
 
w, n = map(int, input().split()) # 배낭의 무게, 귀금속 종류
 
metal = [list(map(int, input().split())) for _ in range(n)] # 금속 무게와 가격을 2차원 배열로 생성
 
metal.sort(key=lambda x: -x[1]) # 2차원 배열을 가격을 기준으로 내림차순 정렬 : 가장 높은 가격을 가진 금속을 가방에 넣어야 하므로
 
max_price = 0 
for m, p in metal: # 금속 무게와 가격으로 반복문을 돌려서 가방의 무게보다 무거우기 전까지 반복하고 가방무게를 넘으면 종료
    if w > m:
        max_price += m * p # 최대 가격 = 금속 무게 * 가격
        w -= m # 가방 무게에서 담은 금속 무게 만큼 빼줘서 초기화
    else:
        max_price += w * p # 가방 무게를 넘으면 그때의 가방 무게 * 가격 을 최대 가격으로 반환하고 종료
        break
 
print(max_price)

# 2차원 배열에서 key값을 기준으로 정렬하는 방법을 몰라서 좀 헤맸습니다...
# sort(key=lambda x: -x[1])