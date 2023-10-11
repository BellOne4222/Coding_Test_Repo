import heapq  # heapq 모듈을 임포트합니다. heapq는 최소 힙(min-heap)을 구현하는 데 사용됩니다.
import sys  # sys 모듈을 임포트합니다. 이 모듈은 표준 입력(stdin)을 읽는 데 사용됩니다.

arr = []  # 빈 리스트 'arr'을 생성합니다. 이 리스트는 최소 힙으로 활용됩니다.

heapq.heapify(arr)  # 'arr' 리스트를 최소 힙으로 변환합니다.

n = int(sys.stdin.readline())  # 사용자로부터 입력을 받아 정수 'n'에 저장합니다. 'n'은 반복 횟수를 나타냅니다.

for _ in range(n):  # 'n'번 반복하는 루프를 시작합니다.
    x = int(sys.stdin.readline())  # 사용자로부터 정수 'x'를 입력 받습니다.

    if x != 0:  # 만약 'x'가 0이 아니라면 다음을 수행합니다.
        heapq.heappush(arr, (abs(x), x))
        # 'arr' 리스트에 (x의 절댓값, x) 형태의 튜플을 추가합니다. 
        # 이때, 절댓값을 우선 순위로 사용하여 최소 힙을 유지합니다.

    else:  # 'x'가 0이라면 다음을 수행합니다.
        if arr:  # 'arr' 리스트에 원소가 존재한다면
            print(heapq.heappop(arr)[1])
            # 'arr'에서 최소값을 꺼내어 출력하고, 해당 튜플의 두 번째 요소인 'x'를 출력합니다.
        else:  # 'arr' 리스트가 비어있다면
            print(0)
            # 아무것도 출력하지 않고 0을 출력합니다.