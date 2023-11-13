import sys

# 입력 받기
n, m = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
numbers.sort()

result = []

# 깊이 우선 탐색 함수 정의
def dfs():
    # 길이가 M인 수열을 찾으면 출력하고 함수 종료
    if len(result) == m:
        print(' '.join(map(str, result)))
        return
    
    for i in range(n):
        result.append(numbers[i])  # 현재 수를 선택하고
        dfs()  # 재귀 호출을 통해 다음 숫자를 선택
        result.pop()  # 백트래킹을 위해 마지막에 선택한 수를 제거하여 다른 경우의 수를 탐색

# 초기 호출
dfs()