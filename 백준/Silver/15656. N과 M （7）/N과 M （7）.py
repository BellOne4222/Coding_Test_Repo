import sys

n,m = map(int,sys.stdin.readline().split())

numbers = list(map(int,sys.stdin.readline().split()))
numbers.sort()

result = []

def dfs():
    if len(result) == m:
        print(' '.join(map(str,result)))
        return
    
    for i in range(n):
        result.append(numbers[i])
        dfs()
        result.pop()
            
dfs()       