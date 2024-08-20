import sys

# N: 입국 심사대의 개수, M: 심사를 받아야 하는 사람의 수
n, m = map(int, sys.stdin.readline().split())

# 각 심사대에서 심사를 하는 데 걸리는 시간을 저장할 리스트
k_lst = []

# 심사 시간을 입력받아 리스트에 저장
for _ in range(n):
    k_lst.append(int(sys.stdin.readline()))

# 심사 시간을 오름차순으로 정렬 
k_lst.sort()

# 이분 탐색의 시작점: 최소 심사 시간 
start = min(k_lst)

# 이분 탐색의 종료점: 최악의 경우 모든 사람을 한 개의 심사대에서 처리하는 경우의 시간
end = max(k_lst) * m

# 결과를 저장할 변수, 초기값은 가능한 가장 큰 값으로 설정
result = float('INF')

# 이분 탐색 시작
while start <= end:
    # 중간 시간(mid)을 계산
    mid = (start + end) // 2
    
    # 현재 mid 시간 내에 심사할 수 있는 사람의 수를 계산
    total_k = 0
    
    for k in k_lst:
        total_k += (mid // k)  # 각 심사대에서 mid 시간 동안 처리할 수 있는 사람의 수를 더함
    
    # 모든 사람을 심사할 수 있는 경우
    if total_k >= m:
        # 가능한 최소 시간을 찾기 위해 result를 갱신
        result = min(result, mid)
        # 더 작은 시간 범위에서 탐색하기 위해 end를 줄임
        end = mid - 1
    else:
        # 시간을 늘려야 모든 사람을 심사할 수 있으므로, start를 늘림
        start = mid + 1

# 최종적으로 최소 시간이 저장된 result 출력
print(result)