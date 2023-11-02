def solution(n, times):
    answer = 0
    
    min_t = times[0]
    max_t = times[0] * n
    
    while True:
        mid = (min_t + max_t) // 2
        cnt = 0
        
        for i in times:
            cnt += mid//i
        
        if cnt < n:
            min_t = mid
        
        elif cnt >= n:
            max_t = mid
        
        if min_t == max_t - 1:
            answer = max_t
            break
        
    return answer