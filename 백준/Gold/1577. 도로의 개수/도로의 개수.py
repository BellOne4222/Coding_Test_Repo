import sys

n,m = map(int, sys.stdin.readline().split())

k = int(sys.stdin.readline())

construction = [[[] for _ in range(m+1)] for _ in range(n+1)]

for _ in range(k):
    a,b,c,d = map(int, sys.stdin.readline().split())
    construction[a][b].append([c,d])
    construction[c][d].append([a,b])

dp_table = [[0 for _ in range(m+1)] for _ in range(n+1)]

dp_table[0][0] = 1

for i in range(n+1):
    for j in range(m+1):
        if (i > 0) and [i-1,j] not in construction[i][j]:
            dp_table[i][j] += dp_table[i-1][j]
        
        if (j > 0) and [i,j-1] not in construction[i][j]:
            dp_table[i][j] += dp_table[i][j-1]

print(dp_table[n][m])
        
