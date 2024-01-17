def solution(n, m, section):
    
    # 처음 롤러 생성
    roller = 1
    
    roller_first = section[0]
    roller_end = roller_first + m - 1
    
    # 만든 롤러로 페인팅 작업
    for i in range(len(section)):
        # 현재 칠하고 있는 범위 내이면
        if roller_first <= section[i] <= roller_end:
            continue
        
        # 칠하지 않는 범위(칠하고 있는 범위 외이면)
        else:
            roller += 1
            roller_first = section[i]
            roller_end = roller_first + m -1
    
    return roller
    
    
    