# [[0,4],[5,10],[6,8],[8,9]] 3 이 반례 때문에 실패..

def solution(targets):
    targets = sorted(targets)
    misails = []
    current = targets[0]
    misails.append(current)
    for i in range(1, len(targets)):
        if targets[i][0] < current[1]:
            continue
        else:
            current = targets[i]
            misails.append(current)
            
    
    result = len(misails)
    return result