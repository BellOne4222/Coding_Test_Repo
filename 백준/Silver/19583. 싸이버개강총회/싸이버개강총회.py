import sys

enter = set()  # 입장 학회원 집합

o_start, o_finish, s_finish = sys.stdin.readline().split()
o_s_clock, o_s_minute = o_start.split(":")
o_s = int(o_s_clock+o_s_minute)
o_f_clock, o_f_minute = o_finish.split(":")
o_f = int(o_f_clock+o_f_minute)
s_f_clock, s_f_minute = s_finish.split(":")
s_f = int(s_f_clock+s_f_minute)
result = 0


while True:
    try:
        time, person = sys.stdin.readline().split()
        clock, minute = time.split(":")
        time = int(clock+minute)

        if time <= o_s:
            enter.add(person)
        elif o_f <= time <= s_f and person in enter:
            # if person in enter:
            enter.remove(person)
            result += 1
    except:
        break


print(result)