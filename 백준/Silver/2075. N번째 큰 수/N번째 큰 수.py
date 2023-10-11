import heapq

n = int(input())

arr = list(map(int,input().split()))

heapq.heapify(arr) # 5 7 9 15 12

for _ in range(n-1):
    lst = list(map(int,input().split()))

    for i in range(len(lst)):
        if arr[0] < lst[i]:
            heapq.heappop(arr)
            heapq.heappush(arr,lst[i])

print(arr[0])