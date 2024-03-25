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
        for i in range(0, switch_num, given_num):
            if i != 0 and i % given_num == 0:
                turn_switch(i)
    
    elif male == 2:
        cur_switch = switches[given_num]
        left_idx = given_num - 1
        right_idx = given_num + 1
        
        while True:
            if left_idx > 0 and right_idx < (switch_num + 1):
                if switches[left_idx] == switches[right_idx]:
                    turn_switch(left_idx)
                    turn_switch(right_idx)
                    left_idx -= 1
                    right_idx += 1
                
                else:
                    turn_switch(given_num)
                    break
            else:
                turn_switch(given_num)
                break

result_idx = 1
while result_idx <= switch_num:
    print(switches[result_idx], end=" ")
    result_idx += 1
    
    if result_idx % 20 == 0:
        print()