# 참고 : https://cocook.tistory.com/104
import sys

#보드를 기울이는 함수로 공의 위치와 이동방향(dx, dy)를 입력으로 받는다.
#거리를 추가해주는 이유는 빨간공과 파란공이 붙어있을 때를 처리해주기 위함
def tilt_moving(x, y, dx, dy):
    m =0 # 거리
    while True:
        if board[x][y] == "O": #공이 목표지점에 오면 종료 
            break
        if board[x][y] == "#":
        	#벽위치 한칸 뒤까지 갈 수 있다.
            x -=dx
            y -=dy
            break
        
        #이동
        x += dx
        y += dy
        #거리를 추가해준다.
        m += 1
    return x, y, m

def bfs():
	#queue가 빌 때까지 돈다.
    while queue: 
        cnt ,r_x, r_y, b_x, b_y = queue.pop(0)
      	
        for i in range(4):
        	# 보드를 기울여서 얻은 새로운 위치와 이동한 거리
            nr_x, nr_y, rd = tilt_moving(r_x, r_y, dx[i], dj[i])
            nb_x, nb_y, bd = tilt_moving(b_x, b_y, dx[i], dj[i])
			
            # 파란 공이 빠지면 실패
            if board[nb_x][nb_y] == "O":
                continue
            # 빨간 공이 빠지면 성공
            if board[nr_x][nr_y] == "O":
                return cnt
                
 			#두 공의 위치가 같다면 같은 행 또는 열에 있었다는 뜻
            if nr_x == nb_x and nr_y == nb_y:
                #이동거리가 파란공이 더 크면 파란공이 더 뒤쪽에서 왔다는 뜻이므로 한칸 뒤로 물러준다.
                if rd < bd: 
                    nb_x, nb_y = nb_x-dx[i], nb_y-dj[i]
                else: 
                    nr_x, nr_y = nr_x-dx[i], nr_y-dj[i]
			
            # 해당 상태를 방문하지 않았다면 체크해주고 queue에 넣어준다.
            if not visited[nr_x][nr_y][nb_x][nb_y]:
                visited[r_x][r_y][b_x][b_y] = 1
                queue.append((cnt +1 , nr_x, nr_y, nb_x, nb_y))
    return -1

#입력을 받는 부분
n,m = map(int, sys.stdin.readline().split())
board =[list(sys.stdin.readline().rstrip()) for _ in range(n)]

#빨간공과 파란공을 찾아서 위치를 저장하고 board에서는 해당 부분을 빈공간으로 만들어준다.
for i in range(n):
    for j in range(m):
        if board[i][j] == "R":
            red_location = (i, j,)
            board[i][j] = "."
        elif board[i][j] =="B":
            blue_location = (i, j,)
            board[i][j] = "."   

#bfs는 동일한 상태에 대해서는 진행하지 않아야하는데 
#구슬 찾기 게임에서 상태는 빨간공과 파란공의 위치에 의해서 결정되기 때문에
#아래처럼 visited를 4 X 4 X 4 X 4 행렬로 구성하였다 
#visited[빨간 공 행][빨간 공 열][파란 공 행][파란 공 열]

visited = [[[[0 for i in range(m)] for i in range(n)] for i in range(m)] for i in range(n)]
visited[red_location[0]][red_location[1]][blue_location[0]][blue_location[1]] =1 # 맨처음 상태를 방문해준다
queue = [(1, red_location[0], red_location[1], blue_location[0], blue_location[1]),]
dx= [1,0,-1,0]
dj= [0,1,0,-1]



print(bfs())