# heapq 모듈과 sys 모듈을 가져옵니다.
import heapq
import sys

# 테스트 케이스의 수를 입력받습니다.
t = int(sys.stdin.readline())

# 각 테스트 케이스를 처리합니다.
for i in range(t):
    # 배열 크기 k를 입력받습니다.
    k = int(sys.stdin.readline())
    
    # 최소 힙과 최대 힙을 초기화합니다.
    min_q, max_q = [], []
    
    # 방문 여부를 저장하는 리스트를 초기화합니다.
    visited = [False] * k

    # k번 반복하여 연산을 수행합니다.
    for j in range(k):
        # 연산과 숫자를 입력받습니다.
        operation, num = sys.stdin.readline().split()

        if operation == 'I':  # 'I' 연산인 경우
            # 최소 힙에 (숫자, 인덱스) 튜플을 추가합니다.
            heapq.heappush(min_q, (int(num), j))
            # 최대 힙에 (-숫자, 인덱스) 튜플을 추가합니다.
            heapq.heappush(max_q, (-int(num), j))
            visited[j] = True  # 해당 인덱스를 방문했음을 표시합니다.

        else:  # 'D' 연산인 경우
            if num == '1':  # 최대값을 삭제하는 경우
                while max_q and not visited[max_q[0][1]]:
                    heapq.heappop(max_q)
                if max_q:
                    visited[max_q[0][1]] = False
                    heapq.heappop(max_q)

            else:  # 최소값을 삭제하는 경우
                while min_q and not visited[min_q[0][1]]:
                    heapq.heappop(min_q)
                if min_q:
                    visited[min_q[0][1]] = False
                    heapq.heappop(min_q)

    # 남아 있는 최소 힙과 최대 힙에서 방문하지 않은 원소를 모두 삭제합니다.
    while min_q and not visited[min_q[0][1]]:
        heapq.heappop(min_q)
    while max_q and not visited[max_q[0][1]]:
        heapq.heappop(max_q)

    # 최소 힙과 최대 힙이 모두 비어있지 않으면 최대값과 최소값을 출력합니다.
    if not min_q or not max_q:
        print("EMPTY")
    else:
        a = -max_q[0][0]  # 최대값을 양수로 변환합니다.
        b = min_q[0][0]  # 최소값
        print("{} {}".format(a, b))