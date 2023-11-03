import sys

# n: 사람 수, m: 보석 수를 입력받음
n, m = list(map(int, sys.stdin.readline().split()))

# jewels: 보석의 크기를 저장하는 리스트, right: 보석 크기 중 가장 큰 값
jewels = []
right = 0

# 보석 크기를 입력받아 jewels 리스트에 저장하고, 가장 큰 보석 크기를 right에 저장
for _ in range(m):
    input_jewel = int(sys.stdin.readline().rstrip())
    jewels.append(input_jewel)
    right = max(right, input_jewel)

answer = right

# 1명 당 나눠줘야 하는 보석 개수의 범위를 정의
# 최소 1개부터 보석함 내 최대 보석 크기(right)까지 나눠줄 수 있음
left = 1

# 이분탐색을 사용하여 보석을 나눠주는 과정
while left <= right:
    # 이분탐색을 위해 중간값인 mid를 계산
    mid = (left + right) // 2

    # 보석 1 종류를 mid만큼 나눠줬을 때 필요한 사람의 수
    give = 0

    # 모든 보석에 대해 mid를 기준으로 나눠줄 사람의 수를 계산
    for jewel in jewels:
        # 몫과 나머지를 구함
        give_jewel = jewel // mid
        remain_jewel = jewel % mid

        give += give_jewel

        # 나머지가 존재하면, 해당 보석을 모두 나눠줘야 하므로 1명 더 추가해야 함
        if remain_jewel > 0:
            give += 1

    # 보석을 아직 모든 사람에게 나눠주지 못했다면, 즉 나눠줘야할 사람이 더 필요하다면
    if give > n:
        left = mid + 1
    # 보석을 n명의 사람에게 전부 나눠줄 수 있다면
    else:
        # 현재 mid 값이 가능한 경우 중 가장 작은 값을 찾기 위해 answer 업데이트
        answer = min(answer, mid)
        right = mid - 1

# 최적의 mid 값을 찾았으므로 해당 값을 출력
print(answer)