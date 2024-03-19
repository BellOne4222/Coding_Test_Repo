import sys

# 입력 함수를 sys.stdin.readline으로 설정하여 입력 속도 향상
input = sys.stdin.readline

# 물건의 개수 N 입력 받기
N = int(input())
# 미리 측정된 비교 결과의 개수 M 입력 받기
M = int(input())

# N+1 x N+1 크기의 2차원 리스트 초기화 (인덱스 1부터 사용하기 위해 N+1 사용)
arr = [[False]*(N+1) for _ in range(N+1)]

# 자기 자신과의 비교는 False로 초기화 (무의미한 비교이므로)
for a in range(1, N+1):
    for b in range(1, N+1):
        if a == b:
            arr[a][b] = False

# 미리 측정된 비교 결과 입력 받기
for _ in range(M):
    a, b = map(int, input().split())
    arr[a][b] = True  # a가 b보다 무거우면 True로 설정

# 플로이드-워셜 알고리즘 적용
# 간접적인 비교 결과를 포함하여 전체 비교 가능성 업데이트
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if arr[i][k] and arr[k][j]:  # i > k, k > j 이면 i > j
                arr[i][j] = True

# 각 물건에 대해 비교 결과를 알 수 없는 물건의 개수 출력
for i in range(1, N+1):
    count = -1  # 자기 자신은 제외하기 위해 -1에서 시작
    for j in range(1, N+1):
        # i와 j를 비교할 수 없으면, 즉 arr[i][j]와 arr[j][i] 둘 다 False이면 count 증가
        if not arr[i][j] and not arr[j][i]:
            count += 1
    print(count)

# 플로이드-워셜 알고리즘을 사용하여 간접적인 비교 결과까지 계산한 후, 
# 각 물건에 대해 비교 결과를 알 수 없는 다른 물건의 개수를 계산하여 출력합니다.