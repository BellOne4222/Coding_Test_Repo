import sys

n,m = map(int, sys.stdin.readline().split())

k_lst = []

for _ in range(n):
    k_lst.append(int(sys.stdin.readline()))

k_lst.sort()

start = min(k_lst)
end = max(k_lst) * m

while start <= end:
    mid = (start + end) // 2
    total_k = 0
    
    for k in k_lst:
        total_k += (mid // k)
    
    if total_k >= m:
        end = mid - 1
    else:
        start = mid + 1

print(mid)
        
        
    





        
        
            
        
             
        
    
    
    