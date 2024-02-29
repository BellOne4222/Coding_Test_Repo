from collections import deque

def bfs(graph, start, visited):
    # BFS 함수 정의
    q = deque()  # 데크 생성
    q.append(start)  # 시작 도시를 큐에 추가
    visited[start] = 1  # 시작 도시를 방문 처리
    while q:  # 큐가 빌 때까지 반복
        cur_path = q.popleft()  # 큐에서 현재 경로를 가져옴

        for idx, item in enumerate(graph[cur_path]):  # 현재 경로와 연결된 도시들을 확인
            if item and visited[idx] == 0:  # 연결되어 있고, 방문하지 않은 도시라면
                visited[idx] = 1  # 방문 처리
                q.append(idx)  # 큐에 추가하여 다음에 방문할 도시로 설정

n = int(input())  # 도시의 수 입력
m = int(input())  # 여행 계획에 속한 도시들의 수 입력

graph = []  # 도시들 간의 연결 정보를 담을 리스트
visited = [0] * n  # 도시 방문 여부를 표시할 리스트 초기화
for _ in range(n):  # 각 도시의 연결 정보 입력
    graph.append(list(map(int, input().split())))
travel_path = list(map(int,input().split()))  # 여행 계획 입력
start = travel_path[0] - 1  # 시작 도시의 인덱스 계산

bfs(graph, start, visited)  # BFS 함수 호출하여 여행 가능 여부 확인
flag = True  # 여행 가능 여부를 나타내는 플래그 초기화
for item in travel_path:  # 여행 계획에 속한 도시들에 대해 반복
    if visited[item-1] == 0:  # 방문하지 않은 도시가 있다면
        flag = False  # 여행이 불가능하므로 플래그를 False로 설정
if flag:  # 모든 도시를 방문했다면
    print('YES')  # 가능한 여행 경로이므로 YES 출력
else:
    print('NO')  # 모든 도시를 방문하지 못했다면 불가능한 여행 경로이므로 NO 출력
