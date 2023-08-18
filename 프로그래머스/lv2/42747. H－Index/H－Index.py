# h를 배열의 최댓값까지 돌리고, 인덱스를 배열의 길이만큼 돌려서 h번 이상 인용된 논문의 개수(cnt)와, h가 같을때 조건이 충족되므로, 그 때의 cnt를 결과로 반환

def solution(citations):
    arr = sorted(citations)
    max_h = 0
    for h in range(max(citations)+1):
        cnt = 0
        for idx in range(len(arr)):
            if arr[idx] >= h: 
                cnt += 1
            if cnt == h:
                max_h = cnt
    return max_h

# 이 문제 설명을 보고서 그제서야 문제를 이해하게 되었습니다....
# [ 1,3,9,7,2,8,5,6,4,0 ]

# 위와 같은 예시가 있습니다.

 

# h번 이상 인용된 논문이 h 편 이상이다는 말은

 

# 1(h) 번 이상 인용된 논문 =   9편  >=  1(h) 편 이상

# 2(h) 번 이상 인용된 논문 =   8편  >=  2(h) 편 이상

# 3(h) 번 이상 인용된 논문 =   7편  >=  3(h) 편 이상

# 4(h) 번 이상 인용된 논문 =   6편  >=  4(h) 편 이상

# 5(h) 번 이상 인용된 논문 =   5편  >=  5(h) 편 이상

# 6(h) 번 이상 인용된 논문 =   4편  <    6(h) 편 미만 
            
            
            
        
                
        
    