import sys

# 입력 받기
n, m = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
numbers = sorted(numbers)

# 조건을 만족하는 길이가 M인 수열을 출력하는 함수
def dfs(depth):
    # M개의 수를 선택했을 때, 결과를 출력하고 종료
    if depth == m:
        print(' '.join(map(str, result)))
        return
    
    # 각 자연수에 대해 선택 여부 확인
    for i in range(n):
        # 이미 선택된 자연수는 건너뛰기
        if numbers[i] in result:
            continue
        
        # 자연수를 선택하고 다음 단계로 진행
        result.append(numbers[i])
        dfs(depth + 1)
        
        # 선택한 자연수를 다시 제거하여 다른 경우의 수를 탐색
        result.pop()

# 선택된 자연수를 저장할 리스트 초기화
result = []

# dfs 함수 호출 (깊이 0부터 시작)
dfs(0)