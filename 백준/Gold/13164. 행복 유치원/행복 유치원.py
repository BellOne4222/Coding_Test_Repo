import sys

n, k = map(int, sys.stdin.readline().split())
students = list(map(int, sys.stdin.readline().split()))

# 각 인접한 원생들의 키 차이를 계산
differences = []
for i in range(1, n):
    differences.append(students[i] - students[i - 1])

# 차이들을 내림차순으로 정렬
differences.sort(reverse=True)

# 가장 큰 차이 K-1개를 선택하여 조로 나눔
# 이 차이들은 무시하므로 나머지 차이들의 합이 최소가 됨
result = sum(differences[k-1:])

print(result)