import sys
from collections import deque

def bfs(x):
    # 가능한 모든 이동 방법을 나타내는 리스트
    dy = [1, -1, a, -a, b, -b, a, b]
    queue = deque()
    queue.append(x)
    visited[x] = True
    
    while queue:
        cur_x = queue.popleft()  # 큐에서 현재 위치를 가져옴
        
        # 모든 이동 방법에 대해 탐색
        for i in range(8):
            if i < 6:
                nx = cur_x + dy[i]  # 현재 위치에서 이동할 다음 위치 계산
            else:
                nx = cur_x * dy[i]
            
            if 0 <= nx <= 100000:  # 다음 위치가 범위 내에 있는지 확인
                if not visited[nx]:  # 다음 위치를 방문하지 않았을 경우
                    visited[nx] = True  # 다음 위치를 방문 표시
                    queue.append(nx)  # 다음 위치를 큐에 추가
                    bridge[nx] = bridge[cur_x] + 1  # 다음 위치의 다리 길이를 현재 위치의 다리 길이 + 1로 업데이트


# 입력 받기
a, b, n, m = map(int, sys.stdin.readline().split())

# 다리 길이를 저장할 리스트 생성
bridge = [0 for _ in range(100001)]
# 방문 여부를 나타내는 리스트 생성
visited = [False for _ in range(100001)]

# BFS 호출
bfs(n)

# 주미에게 도달하는 최소 이동 횟수 출력
print(bridge[m])