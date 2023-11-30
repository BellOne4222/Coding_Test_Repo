size = 3
black = '*'
white = '.'
dy = [0, -1, 0, 1, 0]
dx = [0, 0, 1, 0, -1]
INF = 987654321

def cal(y, x, map):
    result = INF
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
    
    result = min(result, cal(next_y, next_x, map[:]))
    
    for k in range(5):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0 <= ny < size and 0 <= nx < size:
            if map[ny][nx] == black:
                map[ny][nx] = white
            else:
                map[ny][nx] = black
    
    result = min(result, cal(next_y, next_x, map[:]) + 1)
    
    for k in range(5):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0 <= ny < size and 0 <= nx < size:
            if map[ny][nx] == black:
                map[ny][nx] = white
            else:
                map[ny][nx] = black
    
    return result


test_cnt = int(input())
for _ in range(test_cnt):
    map = [list(input().strip()) for _ in range(size)]
    result = cal(0, 0, map)
    print(result)

