import sys

n,m = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
numbers = sorted(numbers)


def dfs(depth):
    if depth == m:
        print(' '.join(map(str,result)))
        return
    
    for i in range(n):
        if numbers[i] in result:
            continue
        result.append(numbers[i])
        dfs(depth+1)
        result.pop()

result = []
dfs(0)

