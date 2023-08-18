# 2814. 최장 경로

# N개의 정점과 M개의 간선으로 구성된 가중치가 없는 무방향 그래프에서의 최장 경로의 길이를 계산하자.

# 정점의 번호는 1번부터 N번까지 순서대로 부여되어 있다.

# 경로에는 같은 정점의 번호가 2번 이상 등장할 수 없으며, 경로 상의 인접한 점들 사이에는 반드시 두 정점을 연결하는 간선이 존재해야 한다.

# 경로의 길이는 경로 상에 등장하는 정점의 개수를 나타낸다.


# [입력]

# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

# 각 테스트 케이스의 첫 번째 줄에는 두 개의 자연수 N M(1 ≤ N ≤ 10, 0 ≤ M ≤ 20)이 주어진다.

# 두 번째 줄부터 M개의 줄에 걸쳐서 그래프의 간선 정보를 나타내는 두 정수 x y(1 ≤ x, y ≤ N)이 주어진다.

# x와 y는 서로 다른 정수이며, 두 정점 사이에 여러 간선이 존재할 수 있다.


# [출력]

# 각 테스트 케이스마다 ‘#x ’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고, 그래프에서의 최장 경로의 길이를 출력한다.

# 1. 모든 위치에서 탐색(dfs) => 방문한 노드개수(max)


def dfs(current, visited): # 현재 위치, 방문한 곳
    global ans
    ans = max(ans, len(visited)) # ans와 방문한 곳 수 중에서 최대값 반환

    for node in neighbor[current]: # 현재 위치와 연결된 이웃 노드들을 하나씩 연결
        if node not in visited: # 방문 안한 노드가 있으면
            dfs(node, visited+[node]) # 방문 처리



T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    neighbor = [[] for _ in range(N+1)] # 이웃 노드들을 빈배열로 만들어서 구현
    for _ in range(M):
        start, end = map(int, input().split()) # 시작 노드와 끝 노드
        neighbor[start].append(end)
        neighbor[end].append(start)
        # [[], [2], [1], []]
        # [[], [2], [1, 3], [2]]

    ans = 0

    for start in range(1, N+1):
        dfs(start, [start]) # 시작하는 위치, 방문한 곳 배열

    print("#{} {}".format(test_case, ans))