def solution(w,h):
    all_square = w * h
    lst = [1, 2, 1]
    minus = 0
    cnt = 0
    idx = 0
    for i in range(h):
        minus += lst[idx]
        cnt += 1
        idx += 1
        if cnt == 3:
            cnt = 0
            idx = 0
            
            
    result = all_square - minus
    return result