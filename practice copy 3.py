# 참고 : https://velog.io/@woosangchul/%EB%B0%B1%EC%A4%80-2151-%EA%B1%B0%EC%9A%B8%EC%84%A4%EC%B9%98-%ED%8C%8C%EC%9D%B4%EC%8D%AC

import sys

from collections import deque

# 집의 크기 N을 입력 받음
N = int(input())

# 집에 대한 정보를 저장할 리스트와 거울을 설치할 수 있는 위치를 저장할 리스트 초기화
listMap = []
listPos = []

# 방향을 나타내는 리스트와 큐 초기화
dx = [0,1,0,-1]
dy = [1,0,-1,0]
q = deque()

# 집 정보 입력 및 거울 설치 가능한 위치 파악
for _ in range(N):
    listMap.append(list(map(lambda x:x, input())))
    for j in range(N):
        if listMap[-1][j] == '!':
            listPos.append((len(listMap)-1, j))

# 시작점과 끝점의 좌표 파악
startPosX, startPosY, endPosX, endPosY = listPos[0][0], listPos[0][1], listPos[1][0], listPos[1][1]

# 초기 거울 설치 및 시작 방향에 대한 큐 초기화
q.append((listPos[0], 0, 0))
q.append((listPos[0], 0, 1))
q.append((listPos[0], 0, 2))
q.append((listPos[0], 0, 3))

# BFS 알고리즘을 통해 거울을 설치하며 최소 거울 개수를 계산하는 과정
while q:
    (posX, posY), mirrorCount, direction = q.popleft()
    
    # 현재 방향으로 진행하면서 거울 설치 가능한 위치까지 이동
    movePosX = posX + dx[direction]
    movePosY = posY + dy[direction]
        
    while 0 <= movePosX < N and 0 <= movePosY < N and listMap[movePosX][movePosY] != '*':
        # 거울 설치 가능한 위치인 경우, 해당 위치에서 2개의 방향으로 진행할 수 있도록 큐에 추가
        if listMap[movePosX][movePosY] == "!":
            if direction == 0 or direction == 2:
                q.append(((movePosX,movePosY), mirrorCount+1, 1))
                q.append(((movePosX,movePosY), mirrorCount+1, 3))
            else:
                q.append(((movePosX,movePosY), mirrorCount+1, 0))
                q.append(((movePosX,movePosY), mirrorCount+1, 2))

        # 목적지에 도달한 경우, 큐를 비우고 종료
        if movePosX == endPosX and movePosY == endPosY:
            q.clear()
            break

        # 다음 이동 위치로 업데이트
        movePosX += dx[direction]
        movePosY += dy[direction]        

# 최소 거울 개수 출력
print(mirrorCount)


# while 0 <= movePosX < N and 0 <= movePosY < N and listMap[movePosX][movePosY] != '*'::

# 현재 위치 (movePosX, movePosY)가 집 내부에 있고, 벽이 아닌 경우까지 반복합니다.
# 이 조건은 현재 위치가 집 내부에 있으며, 벽이 아니라는 조건을 만족할 때까지 반복합니다.

# if listMap[movePosX][movePosY] == "!"::

# 현재 위치에 거울을 설치할 수 있는 경우를 확인합니다.
# !는 거울을 설치할 수 있는 위치를 나타냅니다.

# if direction == 0 or direction == 2::

# 현재 방향이 가로 방향일 경우입니다.
# 따라서 수직 방향으로 빛을 반사시킬 수 있도록, 즉, 위 아래로 이동할 수 있도록 거울을 설치해야 합니다.
# mirrorCount+1은 거울을 추가로 설치하는 횟수를 나타내며, 1 또는 3 방향으로 거울을 설치하여 다음 위치를 큐에 추가합니다.

# else::

# 현재 방향이 세로 방향일 경우입니다.
# 따라서 수평 방향으로 빛을 반사시킬 수 있도록, 즉, 좌우로 이동할 수 있도록 거울을 설치해야 합니다.
# mirrorCount+1은 거울을 추가로 설치하는 횟수를 나타내며, 0 또는 2 방향으로 거울을 설치하여 다음 위치를 큐에 추가합니다.

# 이 코드 부분은 거울을 설치하여 빛을 반사하는 과정을 담당합니다. 거울을 설치할 수 있는 위치에서는 두 가지 방향으로 빛을 반사시켜 다음 위치를 큐에 추가하고, 
# 이를 반복하여 한 쪽 문에서 다른 쪽 문을 볼 수 있는 최소 거울 개수를 계산합니다.