def what_is_longest(graph, n):
    part = 0
    for i in range(n):
        pair = 1 # 연속 개수 
        for j in range(1,n):
            if graph[i][j] == graph[i][j-1]:
                pair += 1
            else:
                pair = 1
            part = max(part, pair)
        
        pair = 1
        for j in range(1,n):
            if graph[j][i] == graph[j-1][i]:
                pair += 1
            else:
                pair = 1
            part = max(part, pair)
    
    return part





n = int(input())

candys = [list(input()) for _ in range(n)]
longest_part = 0 # 가장 긴 연속한 부분의 길이


for i in range(n):
    for j in range(n):
        # 지금 칸과 인접한 칸을 비교해야하기 때문에 다음 칸이 범위 안에 있을 수 있도록 설정
        if (j+1) < n:
            candys[i][j], candys[i][j+1] = candys[i][j+1], candys[i][j]

            compare = what_is_longest(candys,n)

            longest_part = max(longest_part, compare)

            candys[i][j], candys[i][j+1] = candys[i][j+1], candys[i][j]
        
        if (i+1) < n:
            candys[i][j], candys[i+1][j] = candys[i+1][j], candys[i][j]

            compare = what_is_longest(candys,n)

            longest_part = max(longest_part, compare)

            candys[i][j], candys[i+1][j] = candys[i+1][j], candys[i][j]

print(longest_part)