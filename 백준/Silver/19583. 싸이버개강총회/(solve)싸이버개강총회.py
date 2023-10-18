import sys

enter = set()  # 입장 학회원 집합
bye = set()

# 개강총회, 총회종료, 스트리밍종료 시간을 입력받습니다.
o_start, o_finish, s_finish = sys.stdin.readline().split()
o_s_clock, o_s_minute = o_start.split(":")
o_s = int(o_s_clock + o_s_minute)  # 개강총회 시작 시간 (시간과 분을 합친 정수)
o_f_clock, o_f_minute = o_finish.split(":")
o_f = int(o_f_clock + o_f_minute)  # 총회종료 시간 (시간과 분을 합친 정수)
s_f_clock, s_f_minute = s_finish.split(":")
s_f = int(s_f_clock + s_f_minute)  # 스트리밍종료 시간 (시간과 분을 합친 정수)
result = 0  # 결과 변수 (입장과 퇴장을 비교한 결과)

while True:
    try:
        # 시간과 학회원을 입력받습니다.
        time, person = sys.stdin.readline().split()
        clock, minute = time.split(":")
        time = int(clock + minute)  # 현재 채팅 시간 (시간과 분을 합친 정수)

        if time <= o_s:
            enter.add(person)  # 개강총회 시작 전에 대화한 학회원을 입장으로 기록
        elif o_f <= time <= s_f:
            bye.add(person)  # 총회종료와 스트리밍종료 사이에 대화한 학회원을 퇴장으로 기록
    except:
        break  # 입력이 끝나면 반복문 종료

# 입장한 학회원과 퇴장한 학회원의 교집합을 계산하여 중복된 학회원 수를 구합니다.
result = len(enter.intersection(bye))

print(result)  # 결과 출력