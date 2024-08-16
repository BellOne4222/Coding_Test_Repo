import sys

n,m = map(int, sys.stdin.readline().split())

dvds = list(map(int , sys.stdin.readline().split()))

start = max(dvds)
end = sum(dvds)
result = 0

while start <= end:
    mid = (start + end) // 2
    
    cnt = 1
    total_dvd = 0
    
    
    for dvd in dvds:
        if total_dvd + dvd > mid:
            cnt += 1
            total_dvd = 0
        total_dvd += dvd 
    
    if cnt  <= m:
        result = mid
        end = mid - 1
    else:
        start = mid + 1

print(result)       
        
          