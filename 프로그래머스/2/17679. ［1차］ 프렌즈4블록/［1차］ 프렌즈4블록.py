# 참고 : https://hoons-dev.tistory.com/49

def check(m, n, board):
    # filter 배열을 생성하여 해당 위치에 블록이 지워져야 하는지 표시
    filter = [[0 for _ in range(n)] for _ in range(m)]
    count = 0
    
    # 2x2 블록을 찾아 filter 배열에 표시
    for i in range(m-1):
        for j in range(n-1):
            a = board[i][j]
            b = board[i][j+1]
            c = board[i+1][j]
            d = board[i+1][j+1]
            if a == b == c == d and a != '0':
                filter[i][j], filter[i][j+1], filter[i+1][j], filter[i+1][j+1] = 1, 1, 1, 1
    
    # filter 배열을 기반으로 블록 지우고 count 증가
    for i in range(m):
        for j in range(n):
            if filter[i][j] == 1:
                count += 1
                board[i][j] = '0'
    
    # 지워진 블록이 없으면 종료
    if count == 0:
        return 0
    
    # 블록이 지워진 후 빈 공간을 채우기
    for i in range(m-2, -1, -1): # 가장 아래쪽에서 두 번째 행부터 판의 맨 위까지 거꾸로 탐색합니다. (맨 아래 행은 이미 탐색이 끝났으므로 제외됩니다.)
        for j in range(n): # 각 행에서 왼쪽부터 오른쪽까지 열을 순서대로 탐색합니다.
            k = i # 현재 탐색 중인 행의 인덱스를 k에 할당합니다.
            while 0 <= k+1 < m and board[k+1][j] == '0': # 현재 위치의 아래 행이 존재하고, 아래 행의 현재 열이 빈 공간('0')일 경우에 반복합니다. 이는 아래로 이동하면서 빈 공간을 찾는 과정입니다.
                k += 1 # 빈 공간을 찾았으므로, k를 1 증가시켜 다음 행으로 이동합니다.
            if k != i: 
                board[k][j] = board[i][j]
                board[i][j] = '0'
            # 빈 공간을 찾은 경우(즉, k가 현재 행 i와 다른 경우)에 실행됩니다.
            # 현재 행의 블록을 아래로 이동시키기 위해, board[k][j] = board[i][j]와 board[i][j] = '0'을 수행합니다.
            # 현재 위치의 블록을 아래로 이동시켜서 빈 공간을 채우는 작업입니다.
            # 이렇게 하면 블록이 지워진 후에 빈 공간을 채우는데, 블록이 아래로 떨어져서 빈 공간을 채우게 됩니다. 이후에 다시 새로운 2x2 블록이 형성되어 지워지는 과정을 반복
                
    return count
    

# check 함수
# filter 배열을 초기화하고, count 변수를 0으로 초기화합니다.
# 이중 반복문을 통해 주어진 판을 탐색하면서 2x2로 같은 모양의 블록을 찾습니다.
# 찾은 경우, 해당 블록의 위치를 filter 배열에 표시하고 count를 증가시킵니다.
# filter 배열을 기반으로 블록을 지우고 count를 반환합니다.


def solution(m, n, board):
    answer = 0
    # 문자열을 2차원 리스트로 변환
    board = list(map(list, board))
    
    # 블록이 더 이상 지워지지 않을 때까지 반복
    while True:
        temp = check(m, n, board)
        # 더 이상 지워질 블록이 없으면 종료
        if temp == 0:
            break
        answer += temp
        
    return answer

# solution 함수
# 주어진 판 정보(board)를 2차원 리스트로 변환합니다.
# check 함수를 호출하여 지워진 블록의 개수를 얻고, 이를 temp에 저장합니다.
# 만약 지워진 블록이 없다면, 반복문을 종료하고 최종 결과를 반환합니다.
# 지워진 블록이 있다면, answer에 그 개수를 더하고, 블록을 지우고 빈 공간을 채우는 과정을 반복합니다.
# 최종적으로 모든 블록이 지워질 때까지 반복하며 answer를 업데이트하고 반환합니다.


# 동작과정: solution 함수는 check 함수를 호출하여 2x2로 같은 모양의 블록을 찾고 지우는 작업을 반복합니다.
# 더 이상 지워질 블록이 없을 때까지 이를 반복하며 answer에 지워진 블록의 개수를 누적합니다.
# 각 단계에서는 블록이 지워지면서 빈 공간이 생기고, 이를 채우는 작업이 이루어집니다.
# 최종적으로 지워진 블록의 총 개수가 answer에 누적되어 반환됩니다.