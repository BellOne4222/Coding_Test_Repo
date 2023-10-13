# sys 모듈을 가져와서 sys.stdin.readline 함수를 input으로 사용합니다.
import sys
input = sys.stdin.readline

# n과 m을 입력받습니다. n은 포켓몬 수, m은 문제 수를 나타냅니다.
n, m = map(int, input().split())

# 포켓몬 이름과 번호를 매핑하는 두 개의 딕셔너리를 생성합니다.
pocketmon_dic = {}

# n번 반복하며 포켓몬 이름을 입력받고, 이름과 번호를 딕셔너리에 저장합니다.
for i in range(1, n + 1):
    name = input().rstrip()  # 포켓몬 이름을 입력받습니다.
    pocketmon_dic[name] = i  # 이름을 번호에 매핑합니다.
    pocketmon_dic[i] = name  # 번호를 이름에 매핑합니다.

# m번 반복하며 문제를 입력받고, 해당 문제에 대한 답을 출력합니다.
for j in range(m):
    what = input().rstrip()  # 문제를 입력받습니다.
    if what.isdigit():  # 입력된 값이 숫자인 경우
        print(pocketmon_dic[int(what)])  # 해당 번호의 포켓몬 이름을 출력합니다.
    else:
        print(pocketmon_dic[what])  # 입력된 이름의 포켓몬 번호를 출력합니다.