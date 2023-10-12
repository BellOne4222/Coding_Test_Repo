import heapq

t = int(input())



for _ in range(t):
    k = int(input())
    # I : 삽입, D : 최댓값 삭제, D-1 : 최솟값 삭제
    arr = []
    heapq.heapify(arr)
    for i in range(k):
        
        operation, num = input().split()
        num = int(num)
        # 삽입
        if operation == "I":
            heapq.heappush(arr, num)
        else:
            # Q가 비어있는데 적용할 연산이 ‘D’라면 이 연산은 무시해도 좋다.
            if len(arr) == 0:
                continue
            else:
                # 최솟값 삭제
                if num == -1:
                    heapq.heappop(arr)
                # 최댓값 삭제
                else:
                    arr.remove(max(arr))
    if len(arr) == 0:
        print("EMPTY")
    else:
        print("{} {}".format(max(arr),min(arr)))