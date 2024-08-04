import sys
import heapq

input = sys.stdin.read

# 입력 읽기
input_data = input().split()
N = int(input_data[0])  # 학급 수
M = int(input_data[1])  # 각 학급의 학생 수

# 각 학급의 학생 능력치를 저장하는 리스트 생성
classes = []
index = 2
for _ in range(N):
    # 각 학급의 학생 능력치를 정렬하여 저장
    classes.append(sorted(map(int, input_data[index:index + M])))
    index += M

# 우선순위 큐(최소 힙) 및 최댓값 초기화
heap = []
max_value = float('-inf')

# 각 학급에서 가장 작은 능력치를 가진 학생을 힙에 삽입
for i in range(N):
    # (능력치, 학급 인덱스, 학생 인덱스) 형태로 저장
    heapq.heappush(heap, (classes[i][0], i, 0))
    max_value = max(max_value, classes[i][0])  # 현재까지의 최대 능력치

# 능력치의 최댓값과 최솟값 차이의 최소값을 계산
min_difference = float('inf')

# 힙을 이용하여 범위의 최소값과 최댓값 차이를 찾음
while True:
    # 힙에서 최솟값을 추출
    min_value, class_idx, student_idx = heapq.heappop(heap)
    
    # 현재까지의 최댓값과 최솟값 차이 계산
    min_difference = min(min_difference, max_value - min_value)

    # 더 이상 해당 학급에서 뽑을 수 있는 학생이 없으면 종료
    if student_idx + 1 >= M:
        break

    # 해당 학급의 다음 학생을 힙에 추가
    next_student_value = classes[class_idx][student_idx + 1]
    heapq.heappush(heap, (next_student_value, class_idx, student_idx + 1))
    
    # 최대 능력치 업데이트
    max_value = max(max_value, next_student_value)

# 결과 출력: 최댓값과 최솟값 차이의 최소값
print(min_difference)
