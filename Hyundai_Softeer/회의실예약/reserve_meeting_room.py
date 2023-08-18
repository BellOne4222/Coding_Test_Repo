# 문제 : https://softeer.ai/practice/info.do?idx=1&eid=626
# 회의실 예약

# 참고 : https://talktato.tistory.com/m/36

# 문제 풀이

# 각 회의실마다 각 시간별로 스케줄을 만들어서 예약이 될 때마다 그 시간엔 예약이 되었다고 입력해준다.

# busy를 사용해서 회의실이 이미 예약 되었는지 체크를 한다.

import sys

n, m = map(int, sys.stdin.readline().split())
room = {sys.stdin.readline().strip(): [False] * 10 for _ in range(n)}

for _ in range(m):
    r, s, e = sys.stdin.readline().split()
    s, e = int(s) - 9, int(e) - 9
    busy = False
    for i in range(s, e):
        if room[r][i]:
            busy = True
            break
    if not busy:
        for i in range(s, e):
            room[r][i] = True
room_names = sorted(list(room.keys()))
for r in room_names:
    print(f'Room {r}:')
    busy = True
    time = []
    index = 0
    while index < 10:
        if room[r][index] == False:
            for j in range(index + 1, 10):
                if room[r][j] == True or (j == 9 and room[r][j] == False):
                    busy = False
                    time.append((index + 9, j + 9))
                    index = j
                    break

        index += 1
    
    if not busy:
        print(f'{len(time)} available:')
        for t in time:
            start, end = str(t[0]).zfill(2), str(t[1]).zfill(2)
            print(f'{start}-{end}')
    else:
        print('Not available')
    if r != room_names[-1]:
        print('-----')