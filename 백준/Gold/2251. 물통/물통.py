import sys
from collections import deque

def solve(a, b, c, A, B, C):
    visited = set()  # 상태를 기록할 집합
    answer = set()   # 유효한 결과를 기록할 집합

    queue = deque([(a, b, c)])
    visited.add((a, b, c))
    
    while queue:
        a, b, c = queue.popleft()
        
        # 첫 번째 물통이 비어 있을 때의 세 번째 물통의 양을 기록
        if a == 0:
            answer.add(c)
        
        # 각 물통의 상태에 따라 물을 부을 수 있는 경우의 수를 탐색
        # C -> A
        if c > 0 and a < A:
            move = min(c, A - a)
            next_state = (a + move, b, c - move)
            if next_state not in visited:
                visited.add(next_state)
                queue.append(next_state)

        # C -> B
        if c > 0 and b < B:
            move = min(c, B - b)
            next_state = (a, b + move, c - move)
            if next_state not in visited:
                visited.add(next_state)
                queue.append(next_state)

        # B -> A
        if b > 0 and a < A:
            move = min(b, A - a)
            next_state = (a + move, b - move, c)
            if next_state not in visited:
                visited.add(next_state)
                queue.append(next_state)

        # B -> C
        if b > 0 and c < C:
            move = min(b, C - c)
            next_state = (a, b - move, c + move)
            if next_state not in visited:
                visited.add(next_state)
                queue.append(next_state)

        # A -> B
        if a > 0 and b < B:
            move = min(a, B - b)
            next_state = (a - move, b + move, c)
            if next_state not in visited:
                visited.add(next_state)
                queue.append(next_state)

        # A -> C
        if a > 0 and c < C:
            move = min(a, C - c)
            next_state = (a - move, b, c + move)
            if next_state not in visited:
                visited.add(next_state)
                queue.append(next_state)
    
    # 결과를 정렬하여 출력
    result = sorted(answer)
    print(" ".join(map(str, result)))

# 입력 받기
A, B, C = map(int, sys.stdin.readline().split())

# 문제 해결 함수 호출
solve(0, 0, C, A, B, C)
