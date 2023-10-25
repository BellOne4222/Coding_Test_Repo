import sys

# k: 케이블의 개수, n: 필요한 케이블의 개수를 입력받음
k, n = map(int, sys.stdin.readline().split())

# cables: 케이블 길이를 저장하는 리스트
cables = []

# k번 반복하면서 케이블 길이를 입력받고 cables 리스트에 추가
for _ in range(k):
    cable = int(sys.stdin.readline().rstrip())
    cables.append(cable)

# cables 리스트를 오름차순으로 정렬
cables = sorted(cables)  # 정렬된 리스트: [457, 539, 743, 802]

# 초기값 설정
nCable = 1  # 가능한 최소 케이블 길이
mCable = max(cables)  # 가능한 최대 케이블 길이

# 이진 탐색 알고리즘을 사용하여 최적의 케이블 길이를 찾음
while nCable <= mCable:
    dCable = (mCable + nCable) // 2  # 중간 케이블 길이 계산
    cableCnt = 0  # 현재 길이의 케이블로 만들 수 있는 개수 초기화

    # 모든 케이블에 대해 현재 길이의 케이블로 몇 개를 만들 수 있는지 계산
    for i in range(len(cables)):
        cableCnt += cables[i] // dCable 

    # 필요한 케이블의 개수와 비교하여 이진 탐색 수행
    if cableCnt < n:
        mCable = dCable - 1
    elif cableCnt >= n:
        nCable = dCable + 1

# 최적의 케이블 길이를 찾았으므로 출력
print(mCable)