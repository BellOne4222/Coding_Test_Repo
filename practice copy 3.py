# 1. 창구수 설정
# 2. 고객 별로 대기 번호를 받은 시각과 상담에 걸리는 시간을 설정
# 3. 생성된 데이터를 이용해 상담 처리 과정을 시뮬레이션
# if len(상담창구) == 0: 즉시 상담
# not 빈 창구 : wait
# end 상담시간 -> 빈창구 +=1
# 전체 고객의 대기시간 합?

N = 2
simulation_data = [[0, 3], [2, 5], [4, 2], [5, 3]]

changgu = [] 

wait = []
timer = 0

wait_time = 0

all_time = simulation_data[-1][0] + simulation_data[-1][1] 

idx = 0

for i in range(all_time+1):
    if wait:
        timer += 1
    if len(changgu) <= N and simulation_data[idx][0] == i:
        changgu.append(simulation_data[idx])
        idx += 1
    elif len(changgu) > N and simulation_data[idx][0] == i:
        wait.append(simulation_data[idx])
    if changgu:
        for j in range(len(changgu)):
            if changgu[j][1] == i:
                changgu.remove(changgu[j][1])
                idx += 1
    # if len(changgu) <= N and simulation_data[idx][0] == i:
    #     if wait:
    #         changgu.append(simulation_data[idx])
    #         timer = 0 
    #         wait.pop(0)
    #     else:
    #         changgu.append(simulation_data[idx])
    #     idx += 1
    # elif len(changgu) > N:
    #     wait.append(simulation_data[idx][0])
    # for j in range(len(changgu)):
    #     if changgu[j][1] == i:
    #         changgu.remove(changgu[j])

    
