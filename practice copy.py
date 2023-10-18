# 개강총회를 시작하기 전에, 학회원의 입장 확인 여부를 확인한다. 학회원의 입장 여부는 개강총회가 시작한 시간 이전에 대화를 한 적이 있는 학회원의 닉네임을 보고 체크한다. 
# 개강총회를 시작하자마자 채팅 기록을 남긴 학회원도 제 시간에 입장이 확인된 것으로 간주한다.

# 개강총회를 끝내고 나서, 스트리밍을 끝낼 때까지 학회원의 퇴장 확인 여부를 확인한다. 학회원의 퇴장 여부는 개강총회가 끝나고 스트리밍이 끝날 때까지 대화를 한 적이 있는 
# 학회원의 닉네임을 보고 체크한다. 개강총회가 끝나자마자 채팅 기록을 남겼거나, 
# 개강총회 스트리밍이 끝나자마자 채팅 기록을 남긴 학회원도 제 시간에 퇴장이 확인된 것으로 간주한다.  

# 단, 00:00부터는 개강총회를 시작하기 전의 대기 시간이며, 개강총회 스트리밍 끝난 시간 이후로 남겨져 있는 채팅 기록은 다른 스트리밍 영상의 채팅 기록으로 간주한다.

enter = set() # 입장 배열
bye = set() # 퇴장 배열

o_start, o_finish, s_finish = input().split()
o_s_clock, o_s_minute = map(int, o_start.split(":"))
o_f_clock, o_f_minute = map(int, o_finish.split(":"))
s_f_clock, s_f_minute = map(int, s_finish.split(":"))

f_clock = [i for i in range(o_f_clock,s_f_clock+1)]
f_minute_1 = [i for i in range(o_f_minute,60)]
f_minute_1 = [i for i in range(0,s_f_minute+1)]

while True:
    chatting = input()
    if chatting == "":
        break
    else:
        time, person = chatting.split()
        clock, minuite = map(int, time.split(":"))

        # 개강총회를 시작하자마자 채팅 기록을 남긴 학회원도 제 시간에 입장이 확인된 것으로 간주한다.
        if clock < o_s_clock or clock == o_s_clock and 0 <= minuite <= o_s_minute:
            enter.add(person)
        # 개강총회를 끝내고 나서, 스트리밍을 끝낼 때까지 학회원의 퇴장 확인 여부를 확인한다. 학회원의 퇴장 여부는 개강총회가 끝나고 스트리밍이 끝날 때까지 대화를 한 적이 있는 
        # 학회원의 닉네임을 보고 체크한다. 개강총회가 끝나자마자 채팅 기록을 남겼거나, 
        # 개강총회 스트리밍이 끝나자마자 채팅 기록을 남긴 학회원도 제 시간에 퇴장이 확인된 것으로 간주한다.  
        elif o_f_clock <= clock < s_f_clock:
            if o_f_minute <= minuite < 60:
                bye.add(person)
        elif clock == s_f_clock:
            if minuite <= s_f_minute:
                bye.add(person)

result = 0
for person in enter:
    if person in bye:
        result += 1

print(result)

