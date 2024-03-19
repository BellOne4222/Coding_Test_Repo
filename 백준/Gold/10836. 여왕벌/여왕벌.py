# 필요한 라이브러리 import
import sys

# 격자의 크기 M과 날짜 수 N을 입력 받음
M, N = map(int, input().split())

# 초기 격자를 생성. 모든 애벌레의 크기는 1로 시작.
L = [[1 for j in range(M)] for i in range(M)]

# 각 날짜별 제일 왼쪽 열과 제일 위쪽 행의 애벌레들이 자라는 정도를 저장할 리스트
day = [0 for i in range(2*M-1)]

# N일 동안 반복
for _ in range(N):
    # 각 날짜별로 0, 1, 2로 자라는 애벌레의 개수를 입력 받음
    z, o, t = map(int, sys.stdin.readline().rstrip().split())
    # 1만큼 자라는 애벌레들을 업데이트
    for i in range(z, z+o):
        day[i] += 1
    # 2만큼 자라는 애벌레들을 업데이트
    for i in range(z+o, 2*M-1):
        day[i] += 2

# 제일 왼쪽 열의 애벌레들을 업데이트
for i in range(M-1, -1, -1):
    L[i][0] += day[M-1-i]

# 제일 위쪽 행의 애벌레들을 업데이트
for j in range(1, M):
    L[0][j] += day[M-1+j]

# 나머지 애벌레들을 업데이트. 바로 위에 있는 애벌레 개수로 갱신
for j in range(1, M):
    for i in range(1, M):
        L[i][j] = L[i-1][j]

# 최종 결과 출력
for i in L:
    print(*i)
