import sys

n,m = map(int, sys.stdin.readline().split())

graph = [[[] for _ in range(n)] for _ in range(n)]

plus = [0,1,2]

dx = [0,-1,-1]
dy = [-1,-1,0]

for _ in range(m):
    plus_lst = list(map(int, sys.stdin.readline().split()))
    idx = 0
    for k in range(len(plus_lst)):
        if plus_lst[k] != 0:
            idx = k
            break
        
    for i in reversed(range(n)):
        if plus_lst[idx] == 0:
            idx += 1
        
        graph[i][0].append(plus[idx])
        plus_lst[idx] = plus_lst[idx] - 1
    
    for j in range(1,n):
        if plus_lst[idx] == 0:
            idx += 1
        
        graph[0][j].append(plus[idx])
        plus_lst[idx] = plus_lst[idx] - 1
    
for l in range(n):
    for o in range(n):
        if l == 0:
            graph[l][o] = sum(graph[l][o]) + 1
        elif l != 0 and o == 0:
            graph[l][o] = sum(graph[l][o]) + 1
        else:
            graph[l][o] = graph[l-1][o]
            

for q in range(n):
    for r in range(n):
        print(graph[q][r], end=" ")
    print()
