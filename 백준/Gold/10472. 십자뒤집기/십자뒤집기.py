SIZE = 3
BLACK = '*'
WHITE = '.'
DY = [0, -1, 0, 1, 0]
DX = [0, 0, 1, 0, -1]
INF = 987654321

def cal(y, x, map):
    result = INF
    if y == SIZE:
        for i in range(SIZE):
            for j in range(SIZE):
                if map[i][j] == BLACK:
                    return INF
        return 0
    
    next_y = y
    next_x = x + 1
    if next_x >= SIZE:
        next_y = y + 1
        next_x = 0
    
    result = min(result, cal(next_y, next_x, map[:]))
    
    for k in range(5):
        ny = y + DY[k]
        nx = x + DX[k]
        if 0 <= ny < SIZE and 0 <= nx < SIZE:
            if map[ny][nx] == BLACK:
                map[ny][nx] = WHITE
            else:
                map[ny][nx] = BLACK
    
    result = min(result, cal(next_y, next_x, map[:]) + 1)
    
    for k in range(5):
        ny = y + DY[k]
        nx = x + DX[k]
        if 0 <= ny < SIZE and 0 <= nx < SIZE:
            if map[ny][nx] == BLACK:
                map[ny][nx] = WHITE
            else:
                map[ny][nx] = BLACK
    
    return result

def main():
    test_cnt = int(input())
    for _ in range(test_cnt):
        map = [list(input().strip()) for _ in range(SIZE)]
        result = cal(0, 0, map)
        print(result)

if __name__ == "__main__":
    main()