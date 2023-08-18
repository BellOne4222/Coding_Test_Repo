def solution(arr):
    LCM = max(arr) # 배열에서 제일 큰수를 최대 공약수 개념으로 가정
    
    while True:
        cnt = 0 # 배열안에 있는 모든 수에 대해 최대 공약수로 나눴을 때의 나머지가 0이여야 하기 때문에
        for i in arr:
            if LCM % i == 0: # 나머지가 0이면 cnt 1 증가
                cnt += 1
            else: # 나머지가 0이 아니면 탈출
                break
        if cnt == len(arr): # cnt가 배열의 길이와 같으면 배열안의 모든 수가 같은 수에 대해서 나머지가 0이라는 의미이므로 탈출
            break
        LCM += 1 # cnt가 배열의 길이가 안되면 최대 공약수 1 증가 시켜서 다시 검사
        
    return LCM
    
        
        
        
    
    
    


    
    
    
            
        
        
        
        
        
            
                