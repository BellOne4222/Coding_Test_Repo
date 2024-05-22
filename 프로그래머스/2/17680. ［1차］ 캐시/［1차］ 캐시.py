from collections import deque

def solution(cacheSize, cities):
    cacheMemory = deque()
    hit = 1
    miss = 5
    total_time = 0
    
    for city in range(len(cities)):
        low_city = cities[city].lower()
        
        if len(cacheMemory) < cacheSize:
            if low_city not in cacheMemory:
                total_time += miss
                cacheMemory.append(low_city)
            else:
                total_time += hit
                cacheMemory.remove(low_city)
                cacheMemory.append(low_city)
            
        else:
            if low_city not in cacheMemory:
                total_time += miss
                cacheMemory.append(low_city)
                cacheMemory.popleft()
            else:
                total_time += hit
                cacheMemory.remove(low_city)
                cacheMemory.append(low_city)
    
    return total_time
            
            
        