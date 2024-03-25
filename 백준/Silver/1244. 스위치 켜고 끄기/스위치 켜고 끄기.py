import sys

def turn_switch(idx):
    if switches[idx] == 0:
        switches[idx] = 1
    elif switches[idx] == 1:
        switches[idx] = 0


switch_num = int(sys.stdin.readline())

origin_switches = [-1]

switches = origin_switches + list(map(int, sys.stdin.readline().split()))

student_num = int(sys.stdin.readline())

for _ in range(student_num):
    male, given_num = map(int, sys.stdin.readline().split())
    
    if male == 1:
        for i in range(1, switch_num//given_num + 1):
            turn_switch(i*given_num)
    
    elif male == 2:
        turn_switch(given_num)
        left_idx = given_num - 1
        right_idx = given_num + 1
        
        while True:
            if left_idx > 0 and right_idx <= switch_num and switches[left_idx] == switches[right_idx]:
                turn_switch(left_idx)
                turn_switch(right_idx)
            else:
                break
            left_idx -= 1
            right_idx += 1

for j in range(1, switch_num+1):
    print(switches[j], end = " ")
    if j % 20 == 0 :
        print()