# 비내림차순이다. -> 수열이 같거나 커지는 순이다. 정렬 이후 시작 index를 기준으로 같은 index이거나 더 큰 index만 탐색한다.

import sys

# 입력 받기
n, m = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
numbers.sort()
result = []

# 깊이 우선 탐색 함수 정의
def dfs(depth):
    # 길이가 M인 수열을 찾으면 출력하고 함수 종료
    if len(result) == m:
        print(' '.join(map(str, result)))
        return
    
    compare = 0  # 중복된 수를 피하기 위한 변수
    for i in range(depth, n):
        # 중복된 수를 피하고 비내림차순 조건을 확인하여 수열에 추가
        if compare != numbers[i]:
            result.append(numbers[i])
            compare = numbers[i]
            dfs(i)  # 재귀 호출을 통해 다음 숫자를 선택
            result.pop()  # 백트래킹을 위해 마지막에 선택한 수를 제거

# 초기 호출
dfs(0)