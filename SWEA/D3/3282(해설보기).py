# 3282. 0/1 Knapsack

# https://ljw538.tistory.com/33

# 민수에게는 1번부터 N번까지의 번호가 부여된 N(1≤N≤100)개의 물건과 최대 K(1≤K≤1000) 부피만큼을 넣을 수 있는 가방이 있다.

# 1번 물건부터 N번 물건 각각은 부피  Vi와 가치 Ci 를 가지고 있다. (1≤Vi, Ci≤100)

# 민수는 물건들 중 몇 개를 선택하여 가방에 넣어서 그 가치의 합을 최대화하려고 한다.

# 단, 선택한 물건들의 부피 합이 K 이하여야 한다.

# 민수가 가방에 담을 수 있는 최대 가치를 계산하자.

# [입력]

# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

# 각 테스트 케이스의 첫째 줄에 물건의 개수와 가방의 부피인 N K가 주어진다.

# 다음 N개의 줄에 걸쳐서 i번 물건의 정보를 나타내는 부피  Vi와 가치 Ci가 주어진다.

# [출력]

# 각 테스트 케이스마다 가방에 담을 수 있는 최대 가치를 출력한다.


# DP 사용
T = int(input())
for test_case in range(1, T+1):
    n,k = map(int,input().split())
    dp = [[0] * (k+1) for _ in range(n+1)]
    items = [list(map(int,input().split())) for _ in range(n)]

    for i in range(1,n+1):
        for j in range(1,k+1):
            if items[i - 1][0] <= j:
                dp[i][j] = max(dp[i - 1][j], items[i - 1][1] + dp[i - 1][j - items[i - 1][0]])
            else:
                dp[i][j] = dp[i - 1][j]
    print("#{} {}".format(test_case, dp[n][k]))


#     💨 냅색알고리즘

# 💨 각 아이템에 대해서 가방의 크기를 0부터 1씩 최대무게까지 늘려가며 계산.

# 💨 가방의 크기가 해당 아이템의 무게보다 작으면 아이템을 넣지 못한다. 이전까지의 무게와 가치 적용

# 💨 가방의 크기가 해당 아이템의 무게보다 크면 아이템을 넣을지 말지 선택한다.

# 💨💨 이전까지의 무게와 가치 vs (이전까지의 무게 - 현재 아이템의 무게)의 가치 + 현재 아이템의 가치



# 입력
T = int(input())
Ns = []
for tc in range(T):
    N, K = map(int, input().split())
    items = [list(map(int, input().split())) for _ in range(N)]
    Ns.append((N, K, items))

# 풀이
results = []

for tc in range(T):
    N, K, items = Ns[tc]
    dp = [[0] * (K + 1) for _ in range(N + 1)]

    for i in range(1, len(dp)):
        v, c = items[i - 1]
        for j in range(1, len(dp[i])):
            # 가방에 아이템이 들어 갈 수 있으면
            if j >= v:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - v] + c)
            else:
                dp[i][j] = dp[i - 1][j]

    results.append(dp[-1][-1])

# 출력
for tc in range(T):
    print(f'#{tc + 1} {results[tc]}')


