from collections import deque  # deque 모듈을 import합니다.

t = int(input())  # 테스트 케이스의 개수를 입력받습니다.

for _ in range(t):  # 각 테스트 케이스에 대한 반복문입니다.
    p = input()  # 명령어 문자열을 입력받습니다.
    n = int(input())  # 배열의 길이를 입력받습니다.
    x = input()[1:-1]  # 배열을 입력받고, 맨 앞과 맨 뒤의 대괄호를 제거합니다.
    nums = x.split(',')  # 배열을 쉼표(,)를 기준으로 분리하여 리스트로 만듭니다.

    queue = deque(nums)  # 분리된 숫자들을 deque로 변환하여 큐를 만듭니다.

    reverse = 0  # R 명령어의 개수를 저장할 변수입니다.
    flag = False  # 에러 발생 여부를 나타내는 플래그입니다.

    if n == 0:  # 배열의 길이가 0인 경우 큐를 빈 리스트로 초기화합니다.
        queue = []

    for i in p:  # 명령어 문자열을 한 글자씩 순회합니다.
        if i == 'R':  # R 명령어인 경우
            reverse += 1  # R 명령어의 개수를 1 증가시킵니다.
        else:  # D 명령어인 경우
            if len(queue) == 0:  # 큐가 비어있는 경우
                print('error')  # 에러 메시지를 출력하고
                flag = True  # 에러 플래그를 True로 설정합니다.
                break  # 반복문을 종료합니다.
            elif reverse % 2 == 1:  # R 명령어가 홀수번 수행되었을 때
                queue.pop()  # 큐의 오른쪽에서 원소를 제거합니다.
            else:
                queue.popleft()  # 큐의 왼쪽에서 원소를 제거합니다.

    if not flag:  # 에러 플래그가 False인 경우
        if reverse % 2 == 1:  # R 명령어가 홀수번 수행되었을 때
            queue.reverse()  # 큐의 순서를 뒤집습니다.
        print('[' + ','.join(queue) + ']')  # 큐에 남아있는 원소들을 문자열로 변환하여 출력합니다.