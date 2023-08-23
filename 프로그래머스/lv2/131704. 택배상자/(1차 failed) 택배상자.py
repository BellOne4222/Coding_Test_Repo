# 밑의 로직대로 구현해서 예제 테스트 케이스 들은 다 통과를 했지만 제출 하고 난 테스트 케이스는 모두 실패...

from collections import deque

def solution(order):
    main = [1,2,3,4,5] # 영재 컨베이어 벨트
    main = deque(main)
    sub = deque() # 보조 컨베이어 벨트
    idx = 0
    box = 0
    

    # 첫 번째 while문은 order[0] == main[0] 때까지 main의 박스들을 sub로 옮겨준다
    while True:
        if order[idx] != main[0]:
            wait = main.popleft()
            sub.appendleft(wait)
        else:
            break
    
    # 두 번째 while은 main[0]과 sub[0]을 order[idx]과 비교하고 둘 중에 하나라도 같으면 트럭에 싣고 비교 대상을 order의 다음 원소로 이동
    # 둘 다 없으면 상차를 그만한다.
    while True:
        if main and order[idx] == main[0]:
            main.popleft()
            box += 1 # 트럭에 싣는다
            idx += 1
        elif sub and order[idx] == sub[0]:
            sub.popleft()
            box += 1
            idx += 1
        # main과 sub 둘 다 택배 기사의 순서와 맞는 상자를 뺄 수 없으면 종료
        else: 
            return box