import heapq

t = int(input())

for i in range(t):
    k = int(input())
    min_q, max_q = [], []
    visited = [False] * k

    for j in range(k):
        operation, num = input().split()

        if operation == 'I':
            heapq.heappush(min_q, (int(num), j))
            heapq.heappush(max_q, (-int(num), j))
            visited[j] = True

        else:
            if num == '1':
                while max_q and not visited[max_q[0][1]]:
                    heapq.heappop(max_q)
                if max_q:
                    visited[max_q[0][1]] = False
                    heapq.heappop(max_q)
            else:
                while min_q and not visited[min_q[0][1]]:
                    heapq.heappop(min_q)
                if min_q:
                    visited[min_q[0][1]] = False
                    heapq.heappop(min_q)

    while min_q and not visited[min_q[0][1]]:
        heapq.heappop(min_q)
    while max_q and not visited[max_q[0][1]]:
        heapq.heappop(max_q)

    if not min_q or not max_q:
        print("EMPTY")
    else:
        a = -max_q[0][0]
        b = min_q[0][0]
        print("{} {}".format(a,b))