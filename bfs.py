import sys
from collections import deque

# 동서남북 4방향으로 이동할 때 사용할 좌표 변화값
d = [[1, 0], [0, 1], [-1, 0], [0, -1]]

# 블록을 탐색하는 BFS 함수 정의
def bfs(y, x):
    queue = deque()
    queue.append([y, x])  # 시작점을 큐에 추가
    visited[y][x] = True  # 시작점을 방문했음을 표시
    count = 1  # 현재 블록의 크기를 나타내는 변수

    while queue:
        r, c = queue.popleft()  # 큐에서 하나의 위치를 꺼냄

        for i in range(4):  # 동서남북 4방향 탐색
            dr = r + d[i][0]  # 다음 위치의 행
            dc = c + d[i][1]  # 다음 위치의 열

            # 다음 위치가 유효한 그리드 내에 있고, 해당 위치가 장애물(1)이며 방문하지 않은 경우
            if (0 <= dr < n and 0 <= dc < n) and blockMap[dr][dc] == 1 and not visited[dr][dc]:
                queue.append([dr, dc])  # 다음 위치를 큐에 추가
                visited[dr][dc] = True  # 다음 위치를 방문했음을 표시
                count += 1  # 블록의 크기 증가

    return count  # 현재 블록의 크기 반환

n = int(sys.stdin.readline())  # 정사각형 모양의 지도의 크기 입력

blockMap = [list(map(int, input())) for _ in range(n)]  # 지도 정보 입력

visited = [[False] * n for _ in range(n)]  # 방문 여부를 나타내는 배열 초기화

result = []  # 블록 별 장애물 수를 저장할 리스트

# 모든 지도를 순회하면서 블록(장애물 그룹)을 찾고, 각 블록에 속하는 장애물 수를 결과 리스트에 추가
for i in range(n):
    for j in range(n):
        if blockMap[i][j] == 1 and not visited[i][j]:
            result.append(bfs(i, j))

print(len(result))  # 블록의 개수 출력

result.sort()  # 블록 크기 리스트를 오름차순으로 정렬

for i in result:
    print(i)  # 각 블록에 속하는 장애물 수 출력