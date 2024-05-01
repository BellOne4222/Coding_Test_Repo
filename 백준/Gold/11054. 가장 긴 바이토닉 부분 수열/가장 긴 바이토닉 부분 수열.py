import sys

# 입력 받기
n = int(sys.stdin.readline().rstrip())  # 수열의 길이 N을 입력 받음
a = list(map(int, sys.stdin.readline().split()))  # 수열 A를 입력 받음

# 동적 프로그래밍 테이블 초기화
increase = [1] * n  # 각 위치에서 끝나는 최대 증가 부분 수열의 길이 저장
decrease = [1] * n  # 각 위치에서 시작하는 최대 감소 부분 수열의 길이 저장

# 증가 부분 수열의 최대 길이 계산
for i in range(n):
    for j in range(i):
        if a[j] < a[i]:
            # a[j]가 a[i]보다 작다면, i 위치에서의 증가 부분 수열은 j 위치에서의 길이에 1을 더한 값이 될 수 있음
            increase[i] = max(increase[i], increase[j] + 1)

# 감소 부분 수열의 최대 길이 계산
for i in reversed(range(n)):
    for j in range(i + 1, n):
        if a[j] < a[i]:
            # a[j]가 a[i]보다 작다면, i 위치에서의 감소 부분 수열은 j 위치에서의 길이에 1을 더한 값이 될 수 있음
            decrease[i] = max(decrease[i], decrease[j] + 1)

# 가장 긴 바이토닉 부분 수열의 길이를 계산
max_length = 0
for i in range(n):
    # i 위치를 정점으로 하는 바이토닉 수열의 길이는 increase[i] + decrease[i] - 1
    # 정점 i가 두 번 계산되므로 1을 빼준다
    max_length = max(max_length, increase[i] + decrease[i] - 1)

# 결과 출력
print(max_length)