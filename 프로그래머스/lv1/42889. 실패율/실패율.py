def solution(N, stages):
    users = len(stages) # 사용자 수
    stages = sorted(stages)  # 게임라운드 정렬
    stage = {i:0 for i in range(1,N+1)} # 각 스테이지 마다의 실패율을 저장하기 위한 딕셔너리
    arr = [ar for ar in range(1,N+1)] # N까지의 스테이지 배열
    
    for j in arr: # 스테이지를 돌면서
        if users == 0: # 앞에서 라운드 마다의 사람을 총 인원에서 빼고 실패율을 계산하기 때문에 인원수가 0일때 경우에는 실패율 0으로 설정(zero error 대비)
            stage[j] = 0
        else:
            fail = (stages.count(j)) / users # 실패율 = 스테이지에 머무른 사람수 / 사용자수
            stage[j] = fail # 딕셔너리의 실패율 값 초기화
            users -= stages.count(j) # 각 라운드 별로 사람들을 빼고 다음 라운드로 진행
    
    result_dict = sorted(stage.items(), key = lambda item: item[1], reverse = True) # lambda를 이용해서 딕셔너리의 key(실패율) 기준으로 내림차순 정렬
    result = [] # 실패율 등수에 따른 스테이지 번호를 반환
    for k in range(len(result_dict)):
        result.append(result_dict[k][0])
    
    return result

    
    
        
    
    
    
    

    
    
    