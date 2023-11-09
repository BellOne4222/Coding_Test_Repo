import sys

n,m = map(int, sys.stdin.readline().split())
result = []

def dfs(x):
    if len(result) == m:
        print(' '.join(map(str, result)))
        return
    
    for i in range(1,n+1):
        if i not in result:
            result.append(i)
            dfs(i+1)
            result.pop()
        

dfs(1)