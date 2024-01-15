def solution(n, m, section):
    
    # 처음 롤러 생성
    roller = 1
    
    roller_first = section[0]
    roller_end = roller_first + m - 1
    
    for i in range(len(section)):
        if roller_first <= section[i] <= roller_end:
            continue
        else:
            roller += 1
            roller_first = section[i]
            roller_end = roller_first + m -1
    
    return roller
    
    
    