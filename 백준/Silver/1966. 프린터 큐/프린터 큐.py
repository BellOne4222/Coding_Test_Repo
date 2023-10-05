# collections 모듈에서 deque를 가져옵니다.
from collections import deque

# 사용자로부터 정수 n을 입력 받습니다.
n = int(input())

# n번 반복합니다.
for i in range(n):
    # 문서 개수(docu)와 큐에서의 위치(location)를 입력 받습니다.
    docu, location = map(int, input().split())

    # 중요도를 나타내는 리스트(order)를 입력 받고, 입력 리스트를 deque 형식으로 변환합니다.
    order = list(map(int, input().split()))
    order = deque(order)

    # 내 문서가 몇 번째로 출력되는지를 저장하는 변수를 초기화합니다.
    my_order = 0

    # 무한 루프를 시작합니다.
    while True:
        # 현재 큐에서 가장 큰 중요도를 찾습니다.
        m = max(order)

        # 큐에서의 위치를 하나 앞으로 이동합니다.
        location -= 1

        # 큐의 첫 번째 문서의 중요도가 가장 큰 중요도와 같다면
        if order[0] == m:
            # 큐에서 첫 번째 문서를 추출하고, 내 문서 순서를 1 증가시킵니다.
            printer = order.popleft()
            my_order += 1

            # 만약 현재 위치(location)가 음수이면 내 문서 순서를 출력하고 루프를 종료합니다.
            if location < 0:
                print(my_order)
                break
        else:
            # 큐를 왼쪽으로 한 칸 회전시킵니다.
            order.rotate(-1)

            # 만약 현재 위치(location)가 음수이면 위치를 큐의 길이 - 1로 설정하여 다시 시작합니다.
            if location < 0:
                location = len(order) - 1