# 참고 : https://velog.io/@soobin519/Python-%EB%B0%B1%EC%A4%80-2631-%EC%A4%84%EC%84%B8%EC%9A%B0%EA%B8%B0

import sys

n = int(sys.stdin.readline())  # 아이들의 수 입력 받기

dp_table = [1] * (n+1)  # 아이들이 번호 순서대로 정렬되는데 필요한 최소 이동 수를 저장할 DP 테이블
nums = [0]  # 입력된 아이들의 번호를 저장할 리스트, 0번째는 더미값

# 각 아이들의 번호 입력 받기
for i in range(n):
    nums.append(int(sys.stdin.readline()))

# 가장 긴 증가하는 부분 수열(LIS)을 찾는 과정
for i in range(1, n+1):
    for j in range(1, i):
        if nums[j] < nums[i]:
            dp_table[i] = max(dp_table[i], dp_table[j]+1)

# 번호 순서대로 정렬하기 위해 옮겨지는 아이들의 최소 수 계산
# 전체 아이들의 수에서 가장 긴 증가하는 부분 수열의 길이를 뺀 값이 옮겨지는 아이들의 최소 수
print(n - max(dp_table))