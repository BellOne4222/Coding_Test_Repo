# 시간 문자열을 정수로 변환하는 과정에서 12시 40분을 분으로 안고치고 그냥 1240 그대로 변환해서 사용했더니 중간에 연산이 틀리는 과정이 생겨서 테스트 케이스에서 몇 개 틀리는 것이 발생해서 실패...

# 시작 시간과 걸리는 시간을 정수로 바꿔주는 함수
def planstoplan(plan):
    name, start, playtime = plan
    start = start.replace(":",'')
    start = int(start)
    playtime = int(playtime)
    return name, start, playtime
    

def solution(plans):
    # 시작 시각을 기준으로 정렬
    plans.sort(key=lambda x: x[1])
    
    # 끝난 과제를 저장할 리스트
    result = []
    
    # 잠시 멈춘 과제를 저장할 리스트
    stop = []
    
    # 진행 중인 과제명, 시작 시간, 걸리는 시간
    proceeding_name, proceeding_start, proceeding_playtime = planstoplan(plans[0])
    
    proceeding_idx = 1
    
    while True:
        
        next_proceeding_name, next_proceeding_start, next_proceeding_playtime = planstoplan(plans[proceeding_idx])
        
        # 다음 과제 시작 시간이 지금 실행하고 있는 과제가 끝나는 시간보다 작다면
        if next_proceeding_start < proceeding_start + proceeding_playtime:
            # 지금 진행중인 과제명과 진행중인 과제를 더 들어야 하는 시간을 같이 stop에 넣어서 멈춤 처리
            stop.append((proceeding_name, (proceeding_start + proceeding_playtime - next_proceeding_start)))
            # 지금 진행중인 과제에서 다음 진행중인 과제로 진행 중 과제 변경
            proceeding_name, proceeding_start, proceeding_playtime = next_proceeding_name, next_proceeding_start, next_proceeding_playtime
            # 다음 과제를 진행하기 위해서 idx 1증가
            proceeding_idx += 1
        # 다음 과제 시작 시간이 지금 실행하고 있는 과제 끝나는 시간보다 작다면
        else:
            # 지금 과제을 다 들을 수 있으므로 완료 처리
            result.append(proceeding_name) 
            
            # 한 과제 완료 후 stop에 과제가 있다면 그 과제를 진행, 없으면 다음 과제 진행
            if stop:
                # 과제를 끝낸 시각에 새로 시작해야 되는 과제와 잠시 멈춰둔 과제가 모두 있다면, 새로 시작해야 하는 과제부터 진행합니다.
                if proceeding_start + proceeding_playtime == next_proceeding_start:
                    proceeding_name, proceeding_start, proceeding_playtime = next_proceeding_name, next_proceeding_start, next_proceeding_playtime
                    proceeding_idx += 1
                else:
                    # 새로 진행해야 하는 과제와 겹치지 않는다면 꺼내서 과제 진행 할수 있게 지금 진행중인 과제로 변경
                    name, more_listen_time = stop.pop()
                    proceeding_name, proceeding_start, proceeding_playtime = name, proceeding_start + proceeding_playtime , more_listen_time
            # stop에 과제가 없으면
            else:
                proceeding_name, proceeding_start, proceeding_playtime = next_proceeding_name, next_proceeding_start, next_proceeding_playtime
                proceeding_idx += 1
        # 전체 과제를 모두 돌았으면 종료
        if proceeding_idx == len(plans):
            result.append(proceeding_name)
            break
    # stop에 과제가 남아있다면 가장 최근에 멈춘 순으로 과제 다시 시작해서 완료 처리
    if stop:
        for homework in range(len(stop)):
            result.append(stop[-1][0])
            stop.pop()
    return result
                
                
                    
                                    
                    
                    
                    
                    
                
                
            
            
            
            
            
            
        
    
            
            
            
            
        
            
    

        
        
        
    
    # 결과 반환
    return result