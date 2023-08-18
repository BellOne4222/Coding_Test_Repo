import sys

n, m = map(int, input().split())

N = [list(map(int, input().split())) for _ in range(n)] # [[거리, 속도]] 형식으로 리스트 받아오기
M = [list(map(int, input().split())) for _ in range(m)]
max_speed = 0

while True:
    if len(N) == 0 or len(M) == 0: # 리스트가 비면 탈출
        break

    distance_difference = M[0][0] - N[0][0] # 거리 길이 차이

    if distance_difference > 0: # 거리 길이 차가 0보다 크면
        over_speed = M[0][1] - N[0][1] # 초과 속도는 M의 속도에서 N의 속도를 뺀 값
        N.pop(0) # N에서 거리를 빼고
        M[0][0] = distance_difference # M[0][0]을 두 길이를 뺀 값으로 바꿔주기
        if max_speed < over_speed: # 최대 초과 속도 초기화
            max_speed = over_speed
        
    elif distance_difference < 0: # 거리 길이 차가 0보다 작으면
        over_speed = M[0][1] - N[0][1] 
        M.pop(0)
        N[0][0] = -distance_difference # N[0][0]을 두 길이를 뺀 값의 - 붙인 값으로 바꿔주기 : 음수가 나오므로
        if max_speed < over_speed:
            max_speed = over_speed

    else: # 거리 길이 차가 0일때
        over_speed = M[0][1] - N[0][1] # 초과 속도는 두 속도를 뺀 값
        M.pop(0) # 거리 차가 같으므로 남는 값이 없기 때문에 M과 N 둘 다 거리 값 제거
        N.pop(0)
        if max_speed < over_speed:
            max_speed = over_speed

if max_speed >= 0:
    print(max_speed)

else: # 최대 초과 속도가 0보다 작으면 0 출력
    max_speed = 0
    print(max_speed)