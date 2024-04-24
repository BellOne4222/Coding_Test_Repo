# 예제 3,4번 통과 x

import sys
from collections import deque

def check_change(wheels, wheel_num):
    change = [0,0,0,0]
    change[wheel_num-1] = 1
    
    if wheel_num == 1:
        for i in range(3):
            if wheels[i][2] != wheels[i+1][6]:
                change[i+1] = 1
    elif wheel_num == 2:
        if wheels[0][6] != wheels[1][2]:
            change[0] = 1
        
        if wheels[1][2] != wheels[2][6]:
            change[2] = 1
        
        if change[2] == 1:
            change[3] = 1
    elif wheel_num == 3:
        if wheels[1][6] != wheels[2][2]:
            change[1] = 1
        
        if wheels[2][2] != wheels[3][6]:
            change[3] = 1
        
        if change[1] == 1:
            change[0] = 1
        
    else:
        for j in reversed(range(1,4)):
            if wheels[j][6] != wheels[j-1][2]:
                change[j-1] = 1
    
    return change

wheels = []

for _ in range(4):
    wheel = list(map(int, sys.stdin.readline().rstrip()))
    wheel = deque(wheel)
    wheels.append(wheel)

k = int(sys.stdin.readline().rstrip())

for _ in range(k):
    wheel_num, direction = map(int, sys.stdin.readline().split())
    chk_change = check_change(wheels, wheel_num)
    
    wheels[wheel_num-1].rotate(direction)
    
    if wheel_num == 1:
        cur_direction = direction
        for k in range(1,3):
            if chk_change[k] == 1:
                if cur_direction == 1:
                    wheels[k].rotate(-1)
                    cur_direction = -1
                elif cur_direction == -1:
                    wheels[k].rotate(1)
                    cur_direction = 1
                
    elif wheel_num == 2:
        if chk_change[0] == 1:
            if direction == 1:
                wheels[0].rotate(-1)
            elif direction == -1:
                wheels[0].rotate(1)
            
        if chk_change[2] == 1:
            if direction == 1:
                wheels[2].rotate(-1)
            elif direction == -1:
                wheels[2].rotate(1)
            
            if chk_change[3] == 1:
                wheels[3].rotate(direction)
                
    elif wheel_num == 3:
        if chk_change[1] == 1:
            if direction == 1:
                wheels[1].rotate(-1)
            elif direction == -1:
                wheels[1].rotate(1)
            
            if chk_change[0] == 1:
                wheels[0].rotate(direction)
            
        if chk_change[3] == 1:
            if direction == 1:
                wheels[3].rotate(-1)
            elif direction == -1:
                wheels[3].rotate(1)
        
    else:
        for l in reversed(range(1,3)):
            cur_direction = direction
            if chk_change[l] == 1:
                if cur_direction == 1:
                    wheels[l].rotate(-1)
                    cur_direction = -1
                elif cur_direction == -1:
                    wheels[l].rotate(1)
                    cur_direction = 1

total_score = 0
score = 1

for w in range(4):
    if wheels[w][0] == 1:
        total_score += score
    
    score *= 2

print(total_score)