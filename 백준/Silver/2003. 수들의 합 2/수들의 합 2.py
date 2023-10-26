import sys

# 사용자로부터 두 정수를 입력받아 N과 M에 저장합니다.
N, M = map(int, sys.stdin.readline().split())

# 사용자로부터 여러 정수를 입력받아 A_lst에 리스트로 저장합니다.
A_lst = list(map(int, sys.stdin.readline().split()))

# 초기화
left = 0  # A_lst에서 합산을 시작할 왼쪽 인덱스
right = 1  # A_lst에서 합산을 시작할 오른쪽 인덱스 (left와 같은 초기값으로 설정)
case = 0  # 합산 결과가 M과 같은 경우의 수를 저장하는 변수

# right가 N을 초과하거나 left가 right를 초과하지 않는 동안 반복합니다.
while right <= N and left <= right:
    # A_lst의 left부터 right-1까지의 요소들의 합을 계산하여 compare 변수에 저장합니다.
    compare = sum(A_lst[left:right])

    # compare가 M과 같다면, case를 증가시키고 right를 1 증가시킵니다.
    if compare == M:
        case += 1
        right += 1
    # compare가 M보다 작다면, right를 1 증가시킵니다.
    elif compare < M:
        right += 1
    # compare가 M보다 크다면, left를 1 증가시킵니다.
    else:
        left += 1

# 합산 결과가 M과 같은 경우의 수를 출력합니다.
print(case)