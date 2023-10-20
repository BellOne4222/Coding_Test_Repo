import sys

# 입력으로 정수 N을 받습니다.
N = int(input())

# 정수들을 입력받아 리스트로 저장하고, 정렬합니다.
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()

# good 변수를 초기화합니다.
good = 0

# 모든 인덱스 i에 대해 반복합니다.
for i in range(N):
    # 현재 인덱스 i를 제외한 나머지 원소로 이루어진 리스트를 생성합니다.
    parts = nums[:i] + nums[i + 1:]
    
    # 왼쪽과 오른쪽 인덱스를 초기화합니다.
    l_idx = 0
    r_idx = len(parts) - 1

    # 현재 원소 nums[i]를 제외한 나머지 원소를 사용하여, 투 포인터 기법을 사용하여
    # 합을 구해서 nums[i]와 비교합니다.
    while l_idx < r_idx:
        compare = parts[l_idx] + parts[r_idx]

        # 합이 nums[i]와 같으면, 이는 우리가 찾는 경우의 수입니다.
        if compare == nums[i]:
            good += 1
            break
        # 합이 nums[i]보다 작다면, 더 큰 값을 얻기 위해 l_idx를 증가시킵니다.
        if compare < nums[i]:
            l_idx += 1
        # 합이 nums[i]보다 크다면, 더 작은 값을 얻기 위해 r_idx를 감소시킵니다.
        else:
            r_idx -= 1

# 가능한 경우의 수를 출력합니다.
print(good)





