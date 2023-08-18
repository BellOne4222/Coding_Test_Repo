def solution(cacheSize, cities):
    cache = []
    cities = [i.lower() for i in cities] # 대소문자 구분 위해서 모두 소문자로 변경해서 배열 초기화
    running_time = 0
    hit = 1
    miss = 5

    if cacheSize != 0: # cache가 비어있을때의 error 방지
        for city in cities:

            if city not in cache: # cache안에 없으면 miss
                if len(cache) < cacheSize:
                    cache.append(city)
                else:
                    cache.pop(0)
                    cache.append(city)
                running_time += miss

            
            else: # 있으면 hit
                cache.pop(cache.index(city))
                cache.append(city)
                running_time += hit
                
    else: # cache가 비어 있을 때
        running_time = len(cities) * 5
        
    return running_time