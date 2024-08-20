import sys

# 입력을 빠르게 처리하기 위해 sys.stdin.readline을 사용합니다.
n, m = map(int, sys.stdin.readline().split())  # 도시의 가로 크기 n과 세로 크기 m을 입력받습니다.

k = int(sys.stdin.readline())  # 공사 중인 도로의 개수를 입력받습니다.

# 공사 중인 도로를 저장할 리스트를 생성합니다.
# construction[i][j]는 위치 (i, j)에서 공사 중인 도로를 저장하는 리스트입니다.
construction = [[[] for _ in range(m+1)] for _ in range(n+1)]

# 공사 중인 도로 정보를 입력받아 저장합니다.
for _ in range(k):
    a, b, c, d = map(int, sys.stdin.readline().split())
    # (a, b)와 (c, d) 사이의 도로가 공사 중이므로 양쪽 위치에 도로 정보를 추가합니다.
    construction[a][b].append([c, d])
    construction[c][d].append([a, b])

# DP 테이블을 초기화합니다.
# dp_table[i][j]는 위치 (i, j)까지 도달할 수 있는 경우의 수를 저장합니다.
dp_table = [[0 for _ in range(m+1)] for _ in range(n+1)]

# 시작점 (0, 0)에서 도달할 수 있는 경우의 수는 1입니다.
dp_table[0][0] = 1

# DP 테이블을 채워 나갑니다.
for i in range(n+1):
    for j in range(m+1):
        # 현재 위치가 0이 아닌 경우에만 위쪽 위치에서의 경로를 고려
        # 현재 위치 (i, j)의 위쪽 위치 (i-1, j)에서 이동해 오는 경우를 처리합니다.
        if i > 0 and [i-1, j] not in construction[i][j]:
            dp_table[i][j] += dp_table[i-1][j]
        
        # 현재 위치 (i, j)의 왼쪽 위치 (i, j-1)에서 이동해 오는 경우를 처리합니다.
        if j > 0 and [i, j-1] not in construction[i][j]:
            dp_table[i][j] += dp_table[i][j-1]

# 도착점 (n, m)까지 도달할 수 있는 경우의 수를 출력합니다.
print(dp_table[n][m])
