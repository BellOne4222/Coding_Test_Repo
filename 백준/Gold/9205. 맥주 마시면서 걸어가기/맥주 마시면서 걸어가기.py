import sys
input = sys.stdin.readline

from collections import deque

def cal_distance(x, y, nx, ny):
    return abs(nx - x) + abs(ny - y)


def bfs():
    if cal_distance(home_x, home_y, rock_x, rock_y) <= 1000:
        visited[n] = True
        return

    que = deque()

    for i in range(len(conveni)):
        temp = cal_distance(home_x, home_y, conveni[i][0], conveni[i][1])
        if temp <= 1000:
            que.append(conveni[i])
            visited[i] = True

    while que:
        cx, cy = que.popleft()
        for i in range(len(conveni)):
            temp = cal_distance(cx, cy, conveni[i][0], conveni[i][1])
            if temp <= 1000 and not visited[i]:
                que.append(conveni[i])
                visited[i] = True

t = int(input())

for _ in range(t):
    n = int(input())
    visited = [False] * (n + 1)
    conveni = []

    home_x, home_y = map(int, input().split())

    for _ in range(n):
        conveni.append([int(a) for a in input().split()])

    rock_x, rock_y = map(int, input().split())
    conveni.append([rock_x, rock_y])

    bfs()

    if visited[n] == True:
        print('happy')
    else:
        print('sad')