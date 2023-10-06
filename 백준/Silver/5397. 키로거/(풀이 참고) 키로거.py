# 참고 : https://reliablecho-programming.tistory.com/102

# 테스트 케이스의 개수를 입력받음
t = int(input())

# 각 테스트 케이스에 대한 반복
for _ in range(t):
    # 왼쪽 스택과 오른쪽 스택을 초기화
    l_list = []
    r_list = []

    # 사용자로부터 문자열을 입력받음
    data = input()

    # 입력받은 문자열을 문자 단위로 처리
    for i in data:
        # 입력 문자가 '-'인 경우, 왼쪽 스택에서 문자를 제거
        if i == '-':
            # 왼쪽 스택이 비어있지 않을 때만 제거
            if l_list:
                l_list.pop()
        # 입력 문자가 '<'인 경우, 왼쪽 스택에서 오른쪽 스택으로 문자 이동
        elif i == '<':
            # 왼쪽 스택이 비어있지 않을 때만 이동
            if l_list:
                r_list.append(l_list.pop())
        # 입력 문자가 '>'인 경우, 오른쪽 스택에서 왼쪽 스택으로 문자 이동
        elif i == '>':
            # 오른쪽 스택이 비어있지 않을 때만 이동
            if r_list:
                l_list.append(r_list.pop())
        # 그 외의 경우, 입력 문자를 왼쪽 스택에 추가
        else:
            l_list.append(i)

    # 왼쪽 스택에 남은 문자와 오른쪽 스택의 역순 문자를 결합하여 결과 문자열 생성
    l_list.extend(reversed(r_list))
    
    # 결과 문자열 출력
    print(''.join(l_list))