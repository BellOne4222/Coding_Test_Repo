# 2001 파리 퇴치

T = int(input())

for a in range(T):
    N, M = map(int, input().split()) # N, M 받기
    arr = [list(map(int, input().split())) for i in range(N)] # arr에 배열 받기

    kills = [] # 파리 죽인 수 받을 리스트 생성
    # 파리채를 내려칠 곳 탐색
    for i in range(N-M+1): # M~N 까지 범위
        for j in range(N-M+1):
            fly = 0 # 파리 개수
            # 해당 위치를 타격했을 때 잡을 수 있는 파리의 수 탐색 
            for k in range(M): # M*M 배열의 [k][l] 칸으로 탐색
                for l in range(M):
                    fly += arr[i+k][j+l] # 칸의 번호 반환
            kills.append(fly)

	# 배열 범위 안에서 가능한 경우의 수 중에서 가장 많은 파리를 잡을 때의 수 출력
    print("#"+str(a+1), max(kills))

#     range(N-M+1) : 파리채를 휘두를 수 있는 공간
# ex) M의 크기가 1일 경우, 모든 배열 공간을 대상으로 탐색할(파리채를 휘두를) 수 있다. 그런데 파리채의 크기가 커지게 되면, 탐색할 수 있는 배열 공간은 줄어들게 된다. 
# 이에 따라 탐색 범위를 조절해줘야 하기 때문에 N-M+1으로 조정하였다.
# N이 5일 때, 파리채(M)이 1일 때 휘두를 수 있는 경우의 수 = 25가지
# 동일한 조건에서 M = 2일 때 휘두를 수 있는 경우의 수 = 16가지
# 동일한 조건에서 M = 3일 때 휘두를 수 있는 경우의 수 = 9가지 ... 
 