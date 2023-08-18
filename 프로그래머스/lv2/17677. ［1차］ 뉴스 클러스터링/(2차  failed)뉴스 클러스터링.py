def solution(str1, str2):
    
    
    
    # 문자열 공백 제거
    str1 = str1.lower()
    str2 = str2.lower()
    
    # 두 문장을 두 글자씩 끊어서 배열 생성
    compare_1 = [] 
    compare_2 = [] 
    for i in range(len(str1)-1):
        if str1[i:i+2].isalpha() == True and str1[i:i+2] not in " ":
            compare_1.append(str1[i:i+2])
    for j in range(len(str2)-1):
        if str2[j:j+2].isalpha() == True and str2[j:j+2] not in " ":
            compare_2.append(str2[j:j+2])
    
    # 교집합 개수, 합집합 개수
    compare_3 = compare_1[:] # compare_1과 똑같은 리스트 생성
    compare_4 = compare_2[:]
    inter = []
    
    # 원본에서 remove하면서 진행하면 값이 사라져서 중간에 error 발생
    for k in compare_1: 
        if k in compare_2:
            inter.append(k)
            compare_3.remove(k)
            compare_4.remove(k)
            
    # 합집합 : 교집합을 뺀 1,2 만이 가지고 있는 원소와 교집합의 합
    un = inter + compare_3 + compare_4
    
    # 자카드 유사도는 집합 간의 유사도를 검사하는 여러 방법 중의 하나로 알려져 있다. 두 집합 A, B 사이의 자카드 유사도 J(A, B)는 두 집합의 교집합 크기를 두 집합의 합집합 크기로 나눈 값으로 정의된다.
    # 집합 A와 집합 B가 모두 공집합일 경우에는 나눗셈이 정의되지 않으니 따로 J(A, B) = 1로 정의한다.
    if len(inter) == 0 and len(un) == 0:
        result =  1 * 65536
    else:
        result = int((len(inter)/len(un))*65536)
        
    return result
        
                
                
            
            
    
    
        
        
    
    