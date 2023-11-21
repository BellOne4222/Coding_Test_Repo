# 참고 : https://claude-u.tistory.com/434

import sys
sys.setrecursionlimit(2000) # 최대 재귀를 늘려줘야 런타임 에러를 피할 수 있다

def dfs(x): # DFS 함수 정의
    visited[x] = True # 방문 체크
    number = numbers[x] # 다음 방문 장소
    if not visited[number]: # 방문하지 않았다면
        dfs(number) # 재귀

for _ in range(int(input())):
    N = int(input())
    numbers = [0] + list(map(int, input().split()))
    visited = [True] + [False] * N # 방문 여부 확인용
    result = 0
    
    for i in range(1, N+1):
        if not visited[i]: # 방문하지 않았다면
            dfs(i) # DFS 실행
            result += 1 # 결과값 += 1
    print(result)


# 사이클이 존재할 때, 해당 사이클의 크기를 구하는 문제다. DFS(깊이 우선 탐색)를 통해 해결할 수 있다.

 

# 1) 방문 여부 확인용 visited 리스트를 만들어준다.

# 2) 1부터 N까지 숫자를 돌아가면서 해당 숫자의 목적지를 visit해준다.

# 3-1) 방문한 숫자의 다음 숫자도 방문하지 않았다면 visit한다.

# 3-2) 방문했다면 result에 1을 더한 뒤 탈출한다.

 

# 해당 문제는 순열에 관한 것이기에


# 위와 같은 순회하지 않는 input은 들어오지 않는다.

# 따라서 무조건 순회한다는 가정하에 푼다.