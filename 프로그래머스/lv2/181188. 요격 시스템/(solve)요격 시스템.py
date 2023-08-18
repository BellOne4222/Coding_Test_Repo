# end 값이 current의 end 값보다 작으면 end값을 더 작은 값으로 갱신하는 방법으로 반례 해결해서 solve!
# [[0,4],[5,10],[6,8],[8,9]] 3
# 정렬을 해서 current에 targets의 첫 번째 값을 넣어놓고, 첫 번째 값의 첫 번째 원소를 start, 두 번째 원소를 end로 설정, targets의 두 번째 값 부터 반복문 돌려서 current의 end 값보다 targets의 start가 더 크면 미사일 개수 하나 추가하고, 
# current를 targets, start와 end도 targets로 갱신
# targets의 start보다 current의 end가 더 큰 경우에는 targets의 end이 current의 end값보다 작으면 더 작은 값으로 end값 갱신하여 반례 해결



def solution(targets):
    targets = sorted(targets) # 처음 범위 부터 시작하기 위해서 targets 정렬
    misail = 1 # 미사일 개수
    current = targets[0] # 현재 범위 설정
    start, end = current[0], current[1] # start, end값 설정
    for i in range(1, len(targets)): # targets의 두 번째 값부터 반복
        if targets[i][0] >= end: # current의 end 값보다 targets의 start가 더 크면 미사일 개수 하나 추가하고, current를 targets, start와 end도 targets로 갱신
            misail += 1
            current = targets[i]
            start, end = current[0], current[1]
        else:
            if targets[i][1] < end: # targets의 start보다 current의 end가 더 큰 경우에는 targets의 end이 current의 end값보다 작으면 더 작은 값으로 end값 갱신
                end = targets[i][1]
    
    return misail
        
        
    
        
        
    