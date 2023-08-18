from collections import deque

def solution(cacheSize, cities):
    cache = deque(maxlen=cacheSize) # maxlen : deque의 최대길이 설정해주는 내장함수
    running_time = 0
    hit = 1
    miss = 5
    for i in cities:
        j = i.lower() # 대소문자 구분을 안하므로 소문자로 변경
        if j in cache:
            cache.remove(j)
            cache.append(j)
            running_time += hit
        else:
            cache.append(j)
            running_time += miss
    return running_time