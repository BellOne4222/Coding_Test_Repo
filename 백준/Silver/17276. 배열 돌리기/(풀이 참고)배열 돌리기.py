# https://velog.io/@jy1999/%EB%B0%B0%EC%97%B4-%EB%8F%8C%EB%A6%AC%EA%B8%B0 참고
# 주 대각선, 부 대각선, 가운데 행, 가운데 열 빼고는 가만히 있으므로 옮겨줄 라인만 고려
# 1. X의 주 대각선을 가운데 행으로 옮긴다.
# tmp[n//2][i] = X[i][i]

# 2. X의 가운데 열을 주 대각선으로 옮긴다.
# tmp[i][i] = X[i][n // 2]

# 3. X의 부 대각선을 가운데 열로 옮긴다.
# tmp[i][n//2] = X[i][(n - 1) - i]

# 4. X의 가운데 행을 X의 부 대각선으로 옮긴다.
# tmp[(n-1)-i][i] = X[n // 2][i]

import sys


def clock(n, X):
    tmp = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        for j in range(n):
            tmp[i][j] = X[i][j]

    for i in range(n):
        # X의 주 대각선을 ((1,1), (2,2), …, (n, n)) 가운데 열 ((n+1)/2 번째 열)로 옮긴다.
        tmp[i][n//2] = X[i][i]
        # X의 가운데 열을 X의 부 대각선으로 ((n, 1), (n-1, 2), …, (1, n)) 옮긴다.
        tmp[i][(n - 1) - i] = X[i][n // 2]
        # X의 부 대각선을 X의 가운데 행 ((n+1)/2번째 행)으로 옮긴다.
        tmp[n // 2][i] = X[(n - 1) - i][i]
        # X의 가운데 행을 X의 주 대각선으로 옮긴다.
        tmp[i][i] = X[n // 2][i]

    return tmp


def notClock(n, X):
    tmp = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        for j in range(n):
            tmp[i][j] = X[i][j]

    for i in range(n):
        # X의 주 대각선을 ((1,1), (2,2), …, (n, n)) 가운데  행 ((n+1)/2 번째 행)로 옮긴다.
        tmp[n//2][i] = X[i][i]
        # X의 가운데 열을 X의 주 대각선으로 ((1, 1), (2, 2), …, (n, n)) 옮긴다.
        tmp[i][i] = X[i][n // 2]
        # X의 부 대각선을 X의 가운데 열 ((n+1)/2번째 열)으로 옮긴다.
        tmp[i][n//2] = X[i][(n - 1) - i]
        # X의 가운데 행을 X의 부 대각선으로 옮긴다.
        tmp[(n-1)-i][i] = X[n // 2][i]

    return tmp


t = int(sys.stdin.readline().rstrip(" "))

for _ in range(t):

    n, degree = map(int, sys.stdin.readline().split(" "))
    X = []

    for j in range(n):
        X.append(list(map(int, sys.stdin.readline().split(" "))))

    degree //= 45
    # 각도가 0보다 작으면 반시계 방향, 0보다 크면 시계 방향
    if degree < 0:
        degree *= -1
        for k in range(degree):
            X = notClock(n, X)
        # printX(X)
    else:
        for k in range(degree):
            X = clock(n, X)
        # printX(X)

    for i in range(n):
        for j in range(n):
            print(X[i][j], end=' ')
        print()