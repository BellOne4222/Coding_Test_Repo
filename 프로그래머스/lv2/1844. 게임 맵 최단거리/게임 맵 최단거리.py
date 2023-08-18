# 책 이것이 코딩테스트다 152p 미로 찾기 문제 참고

# deque를 이용한 bfs 동작 방식
# 1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다.
# 2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입 하고 방문 처리를 한다.
# 3. while 문으로 더 이상 수행할 수 없을때 까지 반복
# 4. 시간 복잡도 : O(N)


from collections import deque

def solution(maps):
    
    # 이동 방향에 따른 x,y 정의
    dx = [1,-1,0,0] # 동서남북
    dy = [0,0,1,-1]
    
    # 가장 가까운 칸부터 가므로 bfs 사용
    def bfs(x,y):
        n = len(maps)
        m = len(maps[0])
        
        # 큐의 FIFO를 이용하여 가까운 노드 탐색 진행
        adventure = deque()
        adventure.append((x,y))
        
        # deque가 빌 때까지 반복
        while adventure:
            x, y = adventure.popleft()
            # 진행 방향을 좌표에 더해서 다음 좌표 생성
            for i in range(4):
                next_x = x + dx[i]
                next_y = y + dy[i]
                
                # 맵 벗어나면 continue 처리
                if next_x < 0 or next_y < 0 or next_x >= n or next_y >= m:
                    continue
                # 벽이 있는 자리 이면 continue 처리
                if maps[next_x][next_y] == 0:
                    continue
                # 벽이 없는 곳이고 방문하지 않은 곳이라면, 시작 위치 길이가 1 이므로 최단 거리 기록
                if maps[next_x][next_y] == 1:
                    maps[next_x][next_y] = maps[x][y] + 1
                    adventure.append((next_x,next_y))
        
        # 상대편 진영까지의 최단 거리 반환
        return maps[n-1][m-1]
    
    
    # 시작 위치에서 부터 bfs 시작
    answer = bfs(0,0)
    
    # 상대편 진영까지 갈 수 없을때는 -1 반환
    if answer == 1:
        answer = -1
        return answer
    else:
        return answer
    
    