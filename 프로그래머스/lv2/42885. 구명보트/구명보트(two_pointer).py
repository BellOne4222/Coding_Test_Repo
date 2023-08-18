# 문제 아이디어를 생각 할 때 가장 무거운 사람과 가벼운 사람부터 태우면서 확인해보자라는 생각으로 접근
# 투 포인터 방식으로 구현을 하였고 가장 가벼운 사람과 무거운 사람을 더했을 때 limit보다 작거나 같으면 boat 하나 사용하고 가벼운 사람 인덱스는 1증가 시키고 무거운 사람 인덱스는 1감소시켜서 교차 될때 까지 반복
# limit 보다 크면 보트에 한명만 탈 수 있으므로 가장 무거운 사람 인덱스를 1 감소 시키고 보트 수 1 증가

def solution(people, limit):
    boat = 0
    people = sorted(people)
    
    LW_idx = 0 # 가장 무게가 가벼운 사람의 인덱스
    HW_idx = len(people) - 1 # 가장 무게가 무거운 사람의 인덱스
    
    while LW_idx < HW_idx:
        # 보트에 두 명을 태우는 경우
        if people[LW_idx] + people[HW_idx] <= limit:
            LW_idx += 1
            HW_idx -= 1
        # 보트에 한 명 밖에 못 태우는 경우
        else:
            HW_idx -= 1
            
        boat += 1
        
    if LW_idx == HW_idx: # 같은 숫자에서 인덱스가 만났을 경우
        boat += 1
    
    return boat


print(solution([70, 50, 80, 50], 100))

            
                
                
        
        
            
        
    

        
        