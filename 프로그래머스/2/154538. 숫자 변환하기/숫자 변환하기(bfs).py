from collections import deque

def solution(x, y, n):
    # dis 배열 초기화: dis[i]는 i까지의 최소 이동 거리를 저장
    dis = [0 for _ in range(y+1)]
    
    # 큐(Q) 초기화 및 시작점 추가
    Q = deque()
    Q.append(x)
    
    # 시작점과 도착점이 이미 같은 경우, 연산이 필요하지 않으므로 0을 반환
    if x == y:
        return 0
    
    # BFS 수행
    while Q:
        # 큐에서 현재 위치(nx)를 꺼내옴
        nx = Q.popleft()
        
        # 가능한 모든 연산에 대해 탐색
        for dir in range(3):
            if dir == 0:
                cur_x = nx * 2
            elif dir == 1:
                cur_x = nx * 3
            else:
                cur_x = nx + n
            
            # 연산 결과가 범위를 벗어나거나 이미 방문한 경우, 무시
            if cur_x > y or dis[cur_x]:
                continue
            
            # 도착점에 도달한 경우, 현재까지의 최소 이동 거리 반환
            if cur_x == y:
                return dis[nx] + 1
            
            # 큐에 새로운 위치 추가 및 최소 이동 거리 갱신
            Q.append(cur_x)
            dis[cur_x] = dis[nx] + 1
    
    # BFS가 끝났는데도 도착점에 도달하지 못한 경우, 변환할 수 없다는 의미로 -1 반환
    return -1

# 초기화:

# dis: 길이 y+1의 배열로, 각 인덱스까지의 최소 이동 거리를 저장합니다. 초기값은 0으로 설정됩니다.
# Q: 큐로 사용될 deque를 초기화하고, 시작점 x를 큐에 추가합니다.
# 시작점과 도착점 확인:

# x와 y가 이미 같은 경우, 연산이 필요하지 않으므로 0을 반환합니다.
# BFS 수행:

# 큐가 비어있을 때까지 다음을 반복합니다.
# 큐에서 현재 위치 nx를 꺼내옵니다.
# 모든 가능한 연산에 대한 탐색:

# 각각의 연산 방향에 대해 nx에 대한 새로운 위치 cur_x를 계산합니다.
# 범위를 벗어나지 않고, 이미 방문한 위치가 아닌 경우에만 탐색을 진행합니다.
# 도착점에 도달한 경우:

# 만약 cur_x가 도착점 y와 같다면, 현재까지의 최소 이동 거리인 dis[nx] + 1을 반환합니다.
# 새로운 위치 큐에 추가 및 최소 이동 거리 갱신:

# cur_x를 큐에 추가하고, dis[cur_x]를 dis[nx] + 1로 갱신합니다.
# 결과 반환:

# BFS가 끝났는데도 도착점에 도달하지 못한 경우, 변환할 수 없다는 의미로 -1을 반환합니다.