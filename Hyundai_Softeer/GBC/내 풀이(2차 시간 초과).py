# 시간 초과 실패

import sys

n, m = map(int, input().split())

N = []
N_speed = []

M = []
M_speed = []



for i in range(n):
    arr_1 = list(map(int, input().split()))
    N.append([arr_1[0]])
    N_speed.append([arr_1[1]])

for j in range(m):
    arr_2 = list(map(int, input().split()))
    M.append([arr_2[0]])
    M_speed.append([arr_2[1]])

max_speed = 0

while True:
    distance_difference = M[0][0] - N[0][0]

    if len(N) == 0 or len(M) == 0:
        break

    if distance_difference > 0:
        over_speed = M_speed[0][0] - N_speed[0][0]
        if max_speed < over_speed:
            max_speed = over_speed
        
        N[0][0] = distance_difference
    
    elif distance_difference < 0:
        over_speed = M_speed[0][0] - N_speed[0][0]
        if max_speed < over_speed:
            max_speed = over_speed
        
        M[0][0] = -distance_difference
    
    else:
        over_speed = M_speed[0][0] - N_speed[0][0]
        if max_speed < over_speed:
            max_speed = over_speed
        N.pop(0)
        M.pop(0)

if max_speed >= 0:
    print(max_speed)

else:
    max_speed = 0
    print(max_speed)
