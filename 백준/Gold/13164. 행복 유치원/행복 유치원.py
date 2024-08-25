import sys

# 입력값 처리: 원생의 수 N과 조의 수 K
n, k = map(int, sys.stdin.readline().split())

# 원생들의 키를 입력받아 리스트로 저장
students = list(map(int, sys.stdin.readline().split()))

# 인접한 원생들 사이의 키 차이를 저장할 리스트
differences = []
for i in range(1, n):
    # 각 인접한 원생들 사이의 키 차이를 계산하여 리스트에 추가
    differences.append(students[i] - students[i - 1])

# 차이들을 내림차순으로 정렬
# 큰 차이들을 제거하기 위해 정렬
differences.sort(reverse=True)

# 가장 큰 차이 K-1개를 제거
# 제거된 차이들은 조 사이의 경계가 되고
# 나머지 차이들의 합이 최소 비용이 된다.
result = sum(differences[k-1:])

# 최종 결과 출력
print(result)
