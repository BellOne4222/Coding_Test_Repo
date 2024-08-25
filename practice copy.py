import sys

n, k = map(int, sys.stdin.readline().split())
students = list(map(int, sys.stdin.readline().split()))

# 각 인접한 원생들의 키 차이를 계산
differences = []
for i in range(1, n):
    differences.append(students[i] - students[i - 1])

# 차이들을 내림차순으로 정렬
differences.sort(reverse=True)

print(differences)