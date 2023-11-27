import sys  # sys 모듈을 불러옵니다.

a, p = map(int, sys.stdin.readline().split())  # 입력값을 받습니다. a는 초기값, p는 제곱 횟수입니다.

non_duplicate = []  # 중복되지 않는 수열을 저장할 빈 리스트를 생성합니다.
non_duplicate.append(str(a))  # 초기값을 문자열로 변환하여 리스트에 추가합니다.

while True:  # 무한 루프를 시작합니다.
    combine = str(non_duplicate[-1])  # 현재 수열의 마지막 값을 문자열로 가져옵니다.
    new_combine = 0  # 새로운 수열의 다음 값을 저장할 변수를 초기화합니다.
    for i in range(len(combine)):  # 현재 수열의 각 자릿수에 대해 아래 과정을 수행합니다.
        part = int(combine[i]) ** p  # 각 자릿수를 P번 제곱한 값을 계산합니다.
        new_combine += part  # 새로운 수열의 다음 값을 누적하여 계산합니다.
    
    new_combine = str(new_combine)  # 새로운 수열의 다음 값을 문자열로 변환합니다.
    if new_combine not in non_duplicate:  # 새로운 수가 이미 수열에 없는 경우:
        non_duplicate.append(new_combine)  # 수열에 새로운 수를 추가합니다.
    else:  # 새로운 수가 이미 수열에 있는 경우:
        result = non_duplicate.index(new_combine)  # 반복 부분의 시작을 나타내는 인덱스를 찾습니다.
        break  # 무한 루프를 종료합니다.

print(result)  # 반복 부분을 제외한 나머지 수의 개수를 출력합니다.