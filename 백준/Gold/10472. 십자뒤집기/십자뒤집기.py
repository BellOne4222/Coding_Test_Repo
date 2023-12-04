# 상수 정의: 보드 크기, 색상, 이동 방향, 무한대 값
size = 3
black = '*'
white = '.'
dy = [0, -1, 0, 1, 0]  # 각 방향에 따른 y 좌표 이동 값 (북, 서, 남, 동, 중심)
dx = [0, 0, 1, 0, -1]  # 각 방향에 따른 x 좌표 이동 값 (북, 서, 남, 동, 중심)
INF = 987654321  # 재귀 함수에서 비교를 위한 무한대 값

# 보드를 모두 흰색으로 바꾸기 위해 필요한 최소 클릭 수를 계산하는 재귀 함수
def cal(y, x, map):
    result = INF
    
    # 기본 경우: y가 보드 크기에 도달하면 보드가 모두 흰색인지 확인하고 적절한 클릭 수를 반환
    if y == size:
        for i in range(size):
            for j in range(size):
                if map[i][j] == black:
                    return INF
        return 0
    
    next_y = y
    next_x = x + 1
    if next_x >= size:
        next_y = y + 1
        next_x = 0
    
    # 현재 셀의 색상을 변경하지 않고 재귀 호출
    result = min(result, cal(next_y, next_x, map[:]))
    
    # 현재 셀과 인접한 셀의 색상을 변경
    for k in range(5):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0 <= ny < size and 0 <= nx < size:
            if map[ny][nx] == black:
                map[ny][nx] = white
            else:
                map[ny][nx] = black
    
    # 현재 셀의 색상을 변경한 후 재귀 호출
    result = min(result, cal(next_y, next_x, map[:]) + 1)
    
    # 색상 변경을 원래대로 되돌림
    for k in range(5):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0 <= ny < size and 0 <= nx < size:
            if map[ny][nx] == black:
                map[ny][nx] = white
            else:
                map[ny][nx] = black
    
    return result

# 테스트 케이스 수 입력
test_cnt = int(input())
for _ in range(test_cnt):
    # 각 테스트 케이스의 초기 보드 구성 입력
    map = [list(input().strip()) for _ in range(size)]
    # 보드를 모두 흰색으로 바꾸기 위한 최소 클릭 수 계산
    result = cal(0, 0, map)
    # 각 테스트 케이스의 결과 출력
    print(result)