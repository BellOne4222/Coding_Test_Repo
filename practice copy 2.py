from collections import deque
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
field_info = []

for _ in range(12):
    field_info.append(list(input()))

def bfs(a, b, c):
    global boom_flag
    boom_list = []
    deq = deque()

    deq.append([a,b])
    boom_list.append([a,b])

    field_check[a][b] = True

    n = 1

    while deq:
        x, y = deq.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < 12 and 0 <= ny < 6:
                if field_info[nx][ny] == c and not field_check[nx][ny]:
                    field_check[nx][ny] = True
                    deq.append([nx,ny])
                    boom_list.append([nx,ny])
                    n += 1

    if n >= 4:
        for b in boom_list:
            field_info[b[0]][b[1]] = '.'

        boom_flag = True

boom_count = 0

while True:
    boom_flag = False

    field_check = [[False] * 6 for _ in range(12)]

    for i in range(12):
        for j in range(6):
            if field_info[i][j] != '.':
                bfs(i,j,field_info[i][j])


    for i in range(6):
        rotate_queue = deque()

        for j in range(11,-1,-1):
            if field_info[j][i] != '.':
                rotate_queue.append(field_info[j][i])

        for j in range(11,-1,-1):
            if rotate_queue:
                field_info[j][i] = rotate_queue.popleft()
            else:
                field_info[j][i] = '.'

    if not boom_flag:
        break
    else:
        boom_count += 1

print(boom_count)