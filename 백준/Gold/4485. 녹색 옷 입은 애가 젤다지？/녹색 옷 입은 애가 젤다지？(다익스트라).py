# 표준 입력으로부터 읽기 위한 입력 설정
import sys
import heapq  # 우선순위 큐 구현을 위한 heapq 라이브러리

input = sys.stdin.readline

n = int(input())
dx = [0, 1, -1, 0]  # x 방향 이동 (오른쪽, 왼쪽)
dy = [1, 0, 0, -1]  # y 방향 이동 (아래, 위)
# 문제 인스턴스를 번호 매기기 위한 카운터
cnt = 0
# 0이 입력될 때까지 반복하여 입력의 끝을 나타냄
while n != 0:
    cnt += 1  # 문제 카운터 증가
    # N x N 동굴 지도를 읽어들임, 각 셀에는 도둑루피의 양이 표시됨
    board = [list(map(int, input().split())) for _ in range(n)]
    # 최소 비용 경로를 기반으로 탐색을 관리하기 위한 우선순위 큐
    heap = []
    # 각 셀에 도달하기 위한 최소 비용을 추적하는 거리 테이블
    dist = [[1e9] * n for _ in range(n)]
    # 시작 지점과 그 초기 비용을 설정
    dist[0][0] = board[0][0]
    # 힙에 시작 셀과 그 비용을 푸시
    heapq.heappush(heap, (board[0][0], 0, 0))

    while heap:
        # 가장 낮은 비용의 셀을 팝
        distance, y, x = heapq.heappop(heap)

        # 목표에 도달하면 결과를 출력하고 다음 케이스를 위해 리셋
        if y == n-1 and x == n-1:
            print("Problem", str(cnt)+":", distance)
            n = int(input())  # 다음 동굴의 크기를 읽음
            break
        # 인접한 셀을 탐색 (위, 아래, 왼쪽, 오른쪽)
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            # 유효한 셀 좌표를 확인
            if 0 <= ny < n and 0 <= nx < n:
                cost = distance + board[ny][nx]  # 이 셀에 도달하기 위한 새로운 비용 계산
                # 새로운 비용이 더 낮은 경우 셀의 비용을 업데이트
                if dist[ny][nx] > cost:
                    dist[ny][nx] = cost
                    # 업데이트된 셀을 힙에 푸시
                    heapq.heappush(heap, (cost, ny, nx))