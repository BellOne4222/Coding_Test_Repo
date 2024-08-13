import sys

t = int(sys.stdin.readline())

for _ in range(t):
    
    n,m = map(int, sys.stdin.readline().split())
    
    a = list(map(int, sys.stdin.readline().rstrip().split()))
    b = list(map(int, sys.stdin.readline().rstrip().split()))
    b.sort()
    
    
    result = 0
    
    for num in a:
        start = 0
        end = m - 1
        
        while start < end:
            mid = (start + end) // 2
            
            if b[mid] <= num:
                start = mid + 1
            else:
                end = mid
        
        if start == 0:
            result += b[0]
        else:
            if num - b[start - 1] > b[start] - num:
                result += b[start]
            else:
                result += b[start - 1]
    
    print(result)