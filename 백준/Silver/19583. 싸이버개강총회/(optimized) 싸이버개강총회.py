import sys

enter = set()  # 입장한 학회원을 저장하는 집합

# 개강총회, 총회 종료, 스트리밍 종료 시간을 입력에서 읽고 처리합니다.
o_start, o_finish, s_finish = sys.stdin.readline().split()
o_s_clock, o_s_minute = o_start.split(":")
o_s = int(o_s_clock + o_s_minute)  # 개강총회 시작 시간을 정수로 변환 (시간과 분을 합친 값)
o_f_clock, o_f_minute = o_finish.split(":")
o_f = int(o_f_clock + o_f_minute)  # 총회 종료 시간을 정수로 변환 (시간과 분을 합친 값)
s_f_clock, s_f_minute = s_finish.split(":")
s_f = int(s_f_clock + s_f_minute)  # 스트리밍 종료 시간을 정수로 변환 (시간과 분을 합친 값)
result = 0  # 결과 변수 (개강총회 중에 입장하고 퇴장한 학회원 수를 저장)

while True:
    try:
        # 시간과 학회원을 입력에서 읽고 처리합니다.
        time, person = sys.stdin.readline().split()
        clock, minute = time.split(":")
        time = int(clock + minute)  # 현재 대화 시간을 정수로 변환 (시간과 분을 합친 값)

        if time <= o_s:
            enter.add(person)  # 개강총회 시작 이전에 대화한 학회원을 '입장'으로 기록
        elif o_f <= time <= s_f:
            # 총회 종료와 스트리밍 종료 사이에 대화한 학회원 중 '입장'에 있는 학회원을 '퇴장'으로 기록
            if person in enter:
                enter.remove(person)
                result += 1  # 퇴장한 학회원 수 증가
    except:
        break  # 입력이 끝나면 반복문 종료

# 개강총회 중에 입장하고 퇴장한 학회원 수를 출력합니다.
print(result)  # 결과 출력