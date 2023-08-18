n, m = map(int, input().split())

room = {}

for i in range(n):
    name = input()
    room[name] = [0] * 18 # 9 ~ 18시 표시용, 1~8은 비워두기

for i in range(m):
    name, start, end = input().split()
    start = int(start)
    end = int(end)
    for j in range(start, end):
        room[name][j] = 1 # room[name] = [0] * 18 에서 시작 시간부터 끝시간까지의 0을 1로 변환(예약 된 시간들은 1)

    room.sorted(room.items()) # 딕셔너리의 값들을 정렬 : 딕셔너리를 리스트로 바꿔주고 아반떼 -> 그랜저 -> 소나타 순으로 출력하기 위해서 정렬

for i in range(n):
    current = 1
    temp = [] # 예약 가능한 시간 받는 배열
    for j in range(9,19): # 배열의 9~18시 구간만 본다 
        if current == 1 and room[i][1][j] == 0: # i인덱스가 name이고 [1]은 0,1이 들어있는 배열, [j]가 0이면
            start_time = j # 0을 시간으로 바꾸기
            current = 0 # 비어있으니까 다음으로 전달해주기 위해서 0변환
        elif current == 0 and room[i][1][j] == 1: # 예약이 되있으면
            end_time = j # 1을 시간으로 바꾸기
            current = 1
            temp.append([start_time, end_time])
    

    print(f'Room {room[i][0]}:') # :앞의 공백을 없애주기 위해 f스트링 print 사용, 중괄호로 감싸주면 변수내용 찍힘
    if len(temp) == 0:
        print('Not available')
    else:
        print(len(temp),'available')
        for j in range(len(temp)):
            print(f'{temp[j][0]:02d}-{temp[j][1]}') # 구간과, :02d는 0을 앞에 두자리만큼 출력
    
    if i != n-1: # 마지막이 아닐때만
        print('-----')


