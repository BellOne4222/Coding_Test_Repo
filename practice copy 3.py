# 참고 : https://fre2-dom.tistory.com/245

import sys

def bfs():
    # 상하좌우 방향 이동을 위한 리스트 설정
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    global moving
    queue = set([(0, 0, board[0][0])])  # 중복 방문 제거를 위한 set 사용

    while queue:
        x, y, route = queue.pop()

        # 현재 말이 지날 수 있는 최대 칸 수 계산
        moving = max(moving, len(route))

        # 상하좌우 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 내에 있고, 해당 알파벳이 경로에 없는 경우 탐색 추가
            if 0 <= nx < r and 0 <= ny < c and board[nx][ny] not in route:
                queue.add((nx, ny, board[nx][ny] + route))

r, c = map(int, sys.stdin.readline().split())

board = []

for _ in range(r):
    line = list(sys.stdin.readline().rstrip())
    board.append(line)

moving = -1  # 말이 지날 수 있는 최대 칸 수 초기화

bfs()  # BFS 탐색 수행하여 최대 칸 수 계산
print(moving)  # 최대 칸 수 출력

# {(1, 0, 'FI')}
# {(1, 0, 'FI'), (0, 1, 'EI')}
# {(1, 1, 'HFI'), (0, 1, 'EI')}
# {(0, 1, 'EHFI'), (0, 1, 'EI')}
# {(0, 1, 'EHFI'), (1, 1, 'HEI')}
# {(0, 1, 'EHFI'), (0, 2, 'FEI'), (1, 1, 'HEI')}
# {(0, 2, 'FEI'), (0, 1, 'EHFI'), (2, 1, 'FHEI')}
# {(0, 2, 'FEI'), (0, 1, 'EHFI'), (2, 1, 'FHEI'), (1, 2, 'FHEI')}
# {(1, 0, 'FHEI'), (0, 2, 'FEI'), (0, 1, 'EHFI'), (2, 1, 'FHEI'), (1, 2, 'FHEI')}
# {(2, 2, 'AFHEI'), (1, 0, 'FHEI'), (0, 2, 'FEI'), (1, 2, 'FHEI')}
# {(2, 2, 'AFHEI'), (1, 0, 'FHEI'), (0, 2, 'FEI')}
# {(1, 3, 'KFHEI'), (2, 2, 'AFHEI'), (1, 0, 'FHEI'), (0, 2, 'FEI')}
# {(2, 2, 'AFHEI'), (1, 0, 'FHEI'), (2, 3, 'LKFHEI'), (0, 2, 'FEI')}
# {(0, 3, 'CKFHEI'), (2, 2, 'AFHEI'), (2, 3, 'LKFHEI'), (0, 2, 'FEI'), (1, 0, 'FHEI')}        
# {(0, 3, 'CKFHEI'), (2, 2, 'AFHEI'), (2, 3, 'LKFHEI'), (0, 2, 'FEI'), (1, 0, 'FHEI'), (1, 4, 'CKFHEI')}
# {(0, 3, 'CKFHEI'), (2, 3, 'LKFHEI'), (0, 2, 'FEI'), (1, 0, 'FHEI'), (3, 2, 'GAFHEI'), (1, 4, 'CKFHEI')}
# {(0, 3, 'CKFHEI'), (2, 3, 'LKFHEI'), (0, 2, 'FEI'), (2, 3, 'LAFHEI'), (1, 0, 'FHEI'), (3, 2, 'GAFHEI'), (1, 4, 'CKFHEI')}
# {(0, 3, 'CKFHEI'), (0, 2, 'FEI'), (3, 3, 'CLKFHEI'), (2, 3, 'LAFHEI'), (1, 0, 'FHEI'), (3, 2, 'GAFHEI'), (1, 4, 'CKFHEI')}
# {(0, 3, 'CKFHEI'), (0, 2, 'FEI'), (3, 3, 'CLKFHEI'), (2, 2, 'ALKFHEI'), (2, 3, 'LAFHEI'), (1, 0, 'FHEI'), (3, 2, 'GAFHEI'), (1, 4, 'CKFHEI')}
# {(0, 3, 'CKFHEI'), (0, 3, 'CFEI'), (3, 3, 'CLKFHEI'), (2, 2, 'ALKFHEI'), (2, 3, 'LAFHEI'), (1, 0, 'FHEI'), (3, 2, 'GAFHEI'), (1, 4, 'CKFHEI')}
# {(0, 3, 'CKFHEI'), (3, 3, 'CLKFHEI'), (2, 2, 'ALKFHEI'), (2, 3, 'LAFHEI'), (1, 0, 'FHEI'), (3, 2, 'GAFHEI'), (1, 4, 'CKFHEI'), (1, 3, 'KCFEI')}
# {(0, 3, 'CKFHEI'), (3, 3, 'CLKFHEI'), (2, 2, 'ALKFHEI'), (2, 3, 'LAFHEI'), (1, 0, 'FHEI'), (3, 2, 'GAFHEI'), (0, 4, 'JCFEI'), (1, 4, 'CKFHEI'), (1, 3, 'KCFEI')}
# {(0, 3, 'CKFHEI'), (3, 2, 'GCLKFHEI'), (2, 2, 'ALKFHEI'), (2, 3, 'LAFHEI'), (1, 0, 'FHEI'), (3, 2, 'GAFHEI'), (0, 4, 'JCFEI'), (1, 4, 'CKFHEI'), (1, 3, 'KCFEI')}
# {(0, 3, 'CKFHEI'), (3, 2, 'GALKFHEI'), (3, 2, 'GCLKFHEI'), (2, 3, 'LAFHEI'), (1, 0, 'FHEI'), (3, 2, 'GAFHEI'), (0, 4, 'JCFEI'), (1, 4, 'CKFHEI'), (1, 3, 'KCFEI')}
# {(0, 3, 'CKFHEI'), (3, 2, 'GALKFHEI'), (3, 2, 'GCLKFHEI'), (1, 0, 'FHEI'), (3, 2, 'GAFHEI'), (0, 4, 'JCFEI'), (3, 3, 'CLAFHEI'), (1, 4, 'CKFHEI'), (1, 3, 'KCFEI')}
# {(0, 3, 'CKFHEI'), (3, 2, 'GALKFHEI'), (1, 3, 'KLAFHEI'), (3, 2, 'GCLKFHEI'), (1, 0, 'FHEI'), (3, 2, 'GAFHEI'), (0, 4, 'JCFEI'), (3, 3, 'CLAFHEI'), (1, 4, 'CKFHEI'), (1, 3, 'KCFEI')}  
# {(0, 3, 'CKFHEI'), (3, 2, 'GALKFHEI'), (4, 2, 'CGAFHEI'), (1, 3, 'KLAFHEI'), (3, 2, 'GCLKFHEI'), (0, 4, 'JCFEI'), (3, 3, 'CLAFHEI'), (1, 4, 'CKFHEI'), (1, 3, 'KCFEI')}
# {(0, 3, 'CKFHEI'), (3, 2, 'GALKFHEI'), (4, 2, 'CGAFHEI'), (1, 3, 'KLAFHEI'), (3, 2, 'GCLKFHEI'), (0, 4, 'JCFEI'), (3, 3, 'CLAFHEI'), (1, 4, 'CKFHEI'), (1, 3, 'KCFEI'), (3, 3, 'CGAFHEI')}
# {(0, 3, 'CKFHEI'), (3, 2, 'GALKFHEI'), (4, 2, 'CGAFHEI'), (1, 3, 'KLAFHEI'), (3, 2, 'GCLAFHEI'), (3, 2, 'GCLKFHEI'), (1, 4, 'CKFHEI'), (1, 3, 'KCFEI'), (3, 3, 'CGAFHEI')}
# {(0, 3, 'CKFHEI'), (3, 2, 'GALKFHEI'), (4, 2, 'CGAFHEI'), (1, 3, 'KLAFHEI'), (3, 2, 'GCLAFHEI'), (3, 2, 'GCLKFHEI'), (0, 4, 'JCKFHEI'), (1, 3, 'KCFEI'), (3, 3, 'CGAFHEI')}
# {(0, 3, 'CKFHEI'), (3, 2, 'GALKFHEI'), (4, 2, 'CGAFHEI'), (1, 3, 'KLAFHEI'), (3, 2, 'GCLAFHEI'), (3, 2, 'GCLKFHEI'), (2, 3, 'LKCFEI'), (0, 4, 'JCKFHEI'), (3, 3, 'CGAFHEI')}
# {(0, 3, 'CKFHEI'), (3, 2, 'GALKFHEI'), (4, 2, 'CGAFHEI'), (1, 3, 'KLAFHEI'), (3, 2, 'GCLKFHEI'), (2, 3, 'LCGAFHEI'), (2, 3, 'LKCFEI'), (0, 4, 'JCKFHEI'), (3, 2, 'GCLAFHEI')}
# {(3, 2, 'GALKFHEI'), (4, 2, 'CGAFHEI'), (1, 3, 'KLAFHEI'), (3, 2, 'GCLKFHEI'), (2, 3, 'LCGAFHEI'), (2, 3, 'LKCFEI'), (0, 4, 'JCKFHEI')}
# {(4, 2, 'CGAFHEI'), (1, 3, 'KLAFHEI'), (3, 2, 'GCLKFHEI'), (2, 3, 'LCGAFHEI'), (2, 3, 'LKCFEI'), (0, 4, 'JCKFHEI'), (4, 2, 'CGALKFHEI')}
# {(4, 2, 'CGAFHEI'), (1, 3, 'KLAFHEI'), (3, 2, 'GCLKFHEI'), (2, 3, 'LCGAFHEI'), (2, 3, 'LKCFEI'), (0, 4, 'JCKFHEI'), (3, 3, 'CGALKFHEI'), (4, 2, 'CGA{(3, 2, 'GCLKFHEI'), (4, 1, 'MCGAFHEI'), (2, 3, 'LCGAFHEI'), (2, 3, 'LKCFEI'), (0, 4, 'JCKFHEI'), (3, 3, 'CGALKFHEI'), (0, 3, 'CKLAFHEI'), (4, 2, 'CGALKFHEI')}
# {(3, 2, 'GCLKFHEI'), (4, 1, 'MCGAFHEI'), (2, 3, 'LCGAFHEI'), (2, 3, 'LKCFEI'), (0, 4, 'JCKFHEI'), (3, 3, 'CGALKFHEI'), (0, 3, 'CKLAFHEI'), (4, 2, 'CGALKFHEI'), (1, 4, 'CKLAFHEI')}
# {(2, 2, 'AGCLKFHEI'), (4, 1, 'MCGAFHEI'), (2, 3, 'LCGAFHEI'), (2, 3, 'LKCFEI'), (0, 4, 'JCKFHEI'), (3, 3, 'CGALKFHEI'), (0, 3, 'CKLAFHEI'), (4, 2, 'CGALKFHEI'), (1, 4, 'CKLAFHEI')}
# {(2, 2, 'AGCLKFHEI'), (2, 3, 'LKCFEI'), (0, 4, 'JCKFHEI'), (3, 3, 'CGALKFHEI'), (0, 3, 'CKLAFHEI'), (4, 2, 'CGALKFHEI'), (1, 3, 'KLCGAFHEI'), (1, 4, 'CKLAFHEI')}
# {(2, 2, 'AGCLKFHEI'), (0, 4, 'JCKFHEI'), (3, 3, 'CGALKFHEI'), (0, 3, 'CKLAFHEI'), (4, 2, 'CGALKFHEI'), (1, 3, 'KLCGAFHEI'), (2, 2, 'ALKCFEI'), (1, 4, 'CKLAFHEI')}
# {(0, 4, 'JCKLAFHEI'), (2, 2, 'AGCLKFHEI'), (4, 2, 'CGALKFHEI'), (1, 3, 'KLCGAFHEI'), (2, 2, 'ALKCFEI'), (1, 4, 'CKLAFHEI')}
# {(0, 4, 'JCKLAFHEI'), (2, 2, 'AGCLKFHEI'), (1, 3, 'KLCGAFHEI'), (2, 2, 'ALKCFEI'), (4, 1, 'MCGALKFHEI'), (1, 4, 'CKLAFHEI')}
# {(0, 4, 'JCKLAFHEI'), (2, 2, 'AGCLKFHEI'), (3, 2, 'GALKCFEI'), (4, 1, 'MCGALKFHEI'), (1, 4, 'CKLAFHEI')}
# {(0, 4, 'JCKLAFHEI'), (2, 2, 'AGCLKFHEI'), (3, 2, 'GALKCFEI')}