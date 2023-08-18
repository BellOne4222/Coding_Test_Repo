# 1959 두 개의 숫자열

# 두 개의 숫자열 비교
# (1) T 번 반복
# (2) N , M 비교 -> 1 : N > M 이면, M 만큼 비교, 2: N < M 이면 N만큼 비교, 3: N = M 이면 한번 크기만큼 비교
# (3) 숫자열 비교는 1: N-M+1번 비교 2: M-N+1번 비교 3: 1번 비교(N or M -1)
# (4) 1: bj[0~M] : aj[0~M] 인덱스 bj의 모든 인덱스 +1 하고 비교 => 반복
# (5) 비교 방식 옮기면서 각 곱의 합을 리스트에 저장하고 max 반환
# (6) 출력

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split()) # N, M을 값 받아옴
    A = list(map(int, input().split())) # A 배열 리스트로 받아옴
    B = list(map(int, input().split())) # B 배열 리스트로 받아옴

    if N > M: # M이 큰 숫자를 가지도록 설정하기 위해 변환을 하였고, N과 M의 순서를 바꾸어서 따라오는 AB의 순서도 바꿔야한다.
        N, M = M, N
        A, B = B, A
    
    max_sum = 0 # 나중에 sum의 max값을 반환해주는 변수 초기화

    for i in range(M-N+1):
        multi = 0 # 각 곱을 저장하기 위한 변수

        for j in range(N):
            multi += A[j] * B[j+i] # j인덱스를 i 값으로 조절(1씩 옮기면서 곱하기때문)

        if multi > max_sum: # max_sum 보다 곱의 값의 합이 클때, max_sum을 최신화
            max_sum = multi

    print("#{} {}".format(test_case, max_sum))

    