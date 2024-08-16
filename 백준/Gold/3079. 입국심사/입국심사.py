import sys

n,m = map(int, sys.stdin.readline().split())

k_lst = []

for _ in range(n):
    k_lst.append(int(sys.stdin.readline()))

k_lst.sort()

start = min(k_lst)
end = max(k_lst) * m

result = float('INF')

while start <= end:
    mid = (start + end) // 2
    total_k = 0
    
    for k in k_lst:
        total_k += (mid // k)
    
    if total_k >= m:
        end = mid - 1
        result = min(result, mid)
    else:
        start = mid + 1

print(result)
        