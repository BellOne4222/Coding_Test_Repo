# 주어진 입력
m, n, board = 4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]
answer = 0

# 판 정보를 2차원 리스트로 변환
board = list(map(list, board))

# 지워진 블록의 개수를 누적할 변수
while True:
    # 해당 위치의 블록이 지워져야 하는지 표시하는 filter 배열 초기화
    filter = [[0 for _ in range(n)] for _ in range(m)]
    count = 0  # 지워진 블록의 개수를 세는 변수 초기화

    # 2x2로 같은 모양의 블록을 찾아 filter 배열에 표시
    for i in range(m-1):
        for j in range(n-1):
            a = board[i][j]
            b = board[i][j+1]
            c = board[i+1][j]
            d = board[i+1][j+1]
            if a == b == c == d and a != '0':
                filter[i][j], filter[i][j+1], filter[i+1][j], filter[i+1][j+1] = 1, 1, 1, 1
    
    # filter 배열을 기반으로 블록을 지우고 count 증가
    for i in range(m):
        for j in range(n):
            if filter[i][j] == 1:
                count += 1
                board[i][j] = '0'
    
    # 지워진 블록이 없으면 종료
    if count == 0:
        temp = 0
    
    # 블록이 지워진 후 빈 공간을 채우기
    for i in range(m-2, -1, -1):
        for j in range(n):
            k = i
            while 0 <= k+1 < m and board[k+1][j] == '0':
                k += 1
            if k != i:
                board[k][j] = board[i][j]
                board[i][j] = '0'
    
    temp = count
    
    # 지워진 블록의 개수를 누적하고, 더 이상 지워질 블록이 없으면 종료
    if temp == 0:
        break
    answer += temp

# 최종적으로 지워진 블록의 총 개수 출력
print(answer)