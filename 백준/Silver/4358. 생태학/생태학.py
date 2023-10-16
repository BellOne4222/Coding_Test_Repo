# sys 모듈을 import하여 표줥 입력 (stdin)을 읽을 수 있도록 합니다.
import sys

# 트리 정보를 저장할 빈 딕셔너리를 생성합니다.
tree_dict = {}

# 나무 개수를 추적할 변수를 초기화합니다.
pyobon = 0

# 무한 루프를 시작합니다.
while True:
    # 표준 입력에서 한 줄을 읽어옵니다.
    tree = sys.stdin.readline().rstrip()

    # 만약 읽어온 줄이 비어있다면 (EOF, 더 이상 입력이 없다면) 루프를 종료합니다.
    if tree == "":
        break

    # 나무 개수를 증가시킵니다.
    pyobon += 1

    # 읽어온 나무가 딕셔너리에 없다면 새로운 항목으로 추가하고 개수를 1로 설정합니다.
    if tree not in tree_dict:
        tree_dict[tree] = 1
    else:
        # 이미 딕셔너리에 있는 나무라면 개수를 1 증가시킵니다.
        tree_dict[tree] += 1

# 나무 종류를 알파벳 순으로 정렬하여 딕셔너리를 다시 만듭니다.
tree_dict = dict(sorted(tree_dict.items()))

# 각 나무 종류의 백분율을 계산하고 소수점 4자리까지 표시하는 루프를 시작합니다.
for i in tree_dict:
    # 나무 종류의 백분율을 계산합니다.
    per = ((tree_dict[i] / pyobon) * 100)

    # 소수점 4자리까지 표시하기 위해 문자열 형식을 지정합니다.
    result = "{:.4f}".format(per)

    # 나무 종류와 해당 백분율을 출력합니다.
    print("{} {}".format(i, result))