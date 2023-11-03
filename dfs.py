import sys
from collections import deque

# DFS 함수를 정의합니다. 이 함수는 시작 지점에서 블록을 탐색하고, 그 블록의 크기를 반환합니다.
def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False  # 그리드 범위를 벗어나면 False 반환
    if grid[x][y] == 1:
        cnt.append(1)  # 현재 위치에 장애물(1)이 있다면 cnt 리스트에 1 추가
        grid[x][y] = 0  # 현재 위치를 방문했음을 표시 (0으로 변경)
        # 상, 하, 좌, 우 방향으로 재귀적으로 탐색을 진행합니다.
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True  # 블록을 발견한 경우 True 반환
    return False  # 현재 위치에 장애물이 없는 경우 False 반환

n = int(sys.stdin.readline().rstrip())  # 정사각형 그리드의 크기를 입력받습니다.

grid = [list(map(int, sys.stdin.readline().rstrip())) for i in range(n)]  # 그리드 정보를 입력받습니다.

cnt = []  # 블록의 크기를 저장할 리스트

result = 0  # 블록의 개수를 저장할 변수

result_lst = []  # 각 블록에 속하는 장애물의 수를 저장할 리스트

# 모든 그리드를 순회하면서 블록(장애물 그룹)을 찾습니다.
for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:  # 블록을 발견하면 결과 블록의 개수를 증가
            result += 1
            result_lst.append(len(cnt))  # 블록에 속하는 장애물의 수를 result_lst에 추가
            cnt = []  # 블록의 크기를 초기화

print(result)  # 블록의 총 개수를 출력합니다.

result_lst.sort()  # 블록 크기 리스트를 오름차순으로 정렬합니다.

for i in result_lst:
    print(i)  # 각 블록에 속하는 장애물의 수를 출력합니다.