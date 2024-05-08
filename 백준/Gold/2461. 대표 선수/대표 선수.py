import sys
import heapq
input = sys.stdin.read

# 입력 읽기
input_data = input().split()
N = int(input_data[0])
M = int(input_data[1])

classes = []
index = 2
for _ in range(N):
    classes.append(sorted(map(int, input_data[index:index + M])))
    index += M

heap = []
max_value = float('-inf')
for i in range(N):
    heapq.heappush(heap, (classes[i][0], i, 0))
    max_value = max(max_value, classes[i][0])

min_difference = float('inf')

# 힙을 이용하여 범위의 최소값과 최댓값 차이를 찾음
while True:
    min_value, class_idx, student_idx = heapq.heappop(heap)
    min_difference = min(min_difference, max_value - min_value)

    # 더 이상 해당 학급에서 뽑을 수 있는 학생이 없다면 종료
    if student_idx + 1 >= M:
        break

    # 해당 학급에서 다음 학생을 힙에 추가
    next_student_value = classes[class_idx][student_idx + 1]
    heapq.heappush(heap, (next_student_value, class_idx, student_idx + 1))
    max_value = max(max_value, next_student_value)


# 결과 출력
print(min_difference)