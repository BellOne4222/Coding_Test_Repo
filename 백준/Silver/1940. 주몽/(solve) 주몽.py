import sys

# 입력에서 첫 번째 줄에 있는 숫자 n을 읽어옵니다.
n = int(sys.stdin.readline().rstrip())

# 입력에서 두 번째 줄에 있는 숫자 m을 읽어옵니다.
m = int(sys.stdin.readline().rstrip())

# 입력에서 세 번째 줄에 있는 숫자들을 읽어와 리스트로 저장합니다.
lst = list(map(int, sys.stdin.readline().split()))

# 리스트 lst를 오름차순으로 정렬합니다.
lst = sorted(lst)  # 예시로 주어진 입력 [4, 5, 1, 3, 7, 2]는 [1, 2, 3, 4, 5, 7]로 정렬됩니다.

# 초기화
left = 0           # 정렬된 리스트의 왼쪽 끝 인덱스를 가리키는 포인터
right = len(lst) - 1  # 정렬된 리스트의 오른쪽 끝 인덱스를 가리키는 포인터
result = 0          # 합이 m이 되는 조합의 개수를 저장하는 변수

# left 포인터가 right 포인터보다 왼쪽에 있을 때까지 반복
while left < right:
    # 현재 left와 right가 가리키는 원소의 합을 계산합니다.
    combine = lst[left] + lst[right]
    
    # 합이 m과 같다면
    if combine == m:
        # 조합을 찾았으므로 결과 변수를 증가시키고 left 포인터를 오른쪽으로 이동합니다.
        result += 1
        left += 1
    
    # 합이 m보다 크다면
    elif combine > m:
        # right 포인터를 왼쪽으로 이동하여 두 수의 합을 줄입니다.
        right -= 1
    
    # 합이 m보다 작다면
    else:
        # left 포인터를 오른쪽으로 이동하여 두 수의 합을 키웁니다.
        left += 1

# 모든 조합을 검사한 후, 합이 m인 조합의 개수가 result에 저장되어 있습니다.

# 결과를 출력
print(result)