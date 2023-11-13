import sys

# 입력 받기
n, m = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
numbers = sorted(numbers)

result = []

def dfs():
    if len(result) == m:
        print(' '.join(map(str,result)))
    
    for i in range(n):
        if len(result) == 0 or numbers[i] >= result[-1]:
            result.append(numbers[i])
            dfs()
            result.pop()

dfs()