import heapq  # heapq 모듈을 임포트합니다. heapq는 최소 힙(min-heap)을 구현하는 데 사용됩니다.

n = int(input())  # 사용자로부터 정수 'n'을 입력 받습니다. 'n'은 입력할 숫자의 개수를 나타냅니다.

arr = list(map(int, input().split()))
# 사용자로부터 공백으로 구분된 숫자들을 입력 받아 리스트 'arr'에 저장합니다.

heapq.heapify(arr)
# 'arr' 리스트를 최소 힙으로 변환합니다. 이 때, 리스트 내의 원소들이 최소 힙 속성을 유지하도록 정렬됩니다.

for _ in range(n - 1):  # 'n-1'번 반복하는 루프를 시작합니다. (마지막 숫자는 결과값으로 출력할 것이므로 제외합니다)
    lst = list(map(int, input().split()))
    # 사용자로부터 공백으로 구분된 숫자들을 입력 받아 리스트 'lst'에 저장합니다.

    for i in range(len(lst)):  # 'lst'의 모든 원소에 대해 반복합니다.
        if arr[0] < lst[i]:  # 'arr'의 최솟값(최소 힙의 루트)보다 'lst[i]'가 크다면
            heapq.heappop(arr)  # 'arr'의 최솟값을 제거합니다.
            heapq.heappush(arr, lst[i])  # 'lst[i]'를 'arr'에 추가합니다.

print(arr[0])  # 최종적으로 'arr'의 최솟값(최소 힙의 루트)을 출력합니다.