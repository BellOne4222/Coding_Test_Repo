import sys
from collections import deque

# BFS 함수 정의
def bfs(s, t, kick):
    q = deque()
    q.append((s, t, kick))  # 초기 상태를 큐에 넣어줌
    
    while q:  # 큐에 원소가 있는 동안 반복
        me, opponent, kicks = q.popleft()  # 큐에서 원소 추출
        
        # 태균이의 점수가 상대방의 점수와 같거나 작을 때만 발차기 진행
        if me <= opponent:
            q.append((me * 2, opponent + 3, kicks + 1))  # A 발차기 시도
            q.append((me + 1, opponent, kicks + 1))      # B 발차기 시도
            
            # 태균이의 점수와 상대방의 점수가 같아지면 발차기 횟수 반환
            if me == opponent:
                return kicks 

# 테스트 케이스 수 입력
c = int(sys.stdin.readline())

# 각 테스트 케이스에 대해 실행
for _ in range(c):
    kick = 0
    # 현재 점수 S와 상대의 점수 T를 입력 받음
    s, t = map(int, sys.stdin.readline().split())
    # BFS 함수 실행하여 최소 발차기 횟수 출력
    print(bfs(s, t, kick))