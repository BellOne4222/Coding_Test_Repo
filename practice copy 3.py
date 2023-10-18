enter = set()  # 입장 학회원 집합
bye = set()    # 퇴장 학회원 집합

o_start, o_finish, s_finish = input().split()
o_s_clock, o_s_minute = map(int, o_start.split(":"))
o_f_clock, o_f_minute = map(int, o_finish.split(":"))
s_f_clock, s_f_minute = map(int, s_finish.split(":"))

while True:
    try:
        chatting = input()
        time, person = chatting.split()
        clock, minute = map(int, time.split(":"))

        if clock < o_s_clock or (clock == o_s_clock and minute <= o_s_minute):
            enter.add(person)
        elif o_f_clock <= clock < s_f_clock:
            if o_f_minute <= minute < 60:
                bye.add(person)
        elif clock == s_f_clock and minute <= s_f_minute:
            bye.add(person)
    except:
        break

result = len(enter.intersection(bye))
print(result)