def solution(str1, str2):
    # 자카드 유사도는 집합 간의 유사도를 검사하는 여러 방법 중의 하나로 알려져 있다. 두 집합 A, B 사이의 자카드 유사도 J(A, B)는 두 집합의 교집합 크기를 두 집합의 합집합 크기로 나눈 값으로 정의된다.
    # result = len(intersection) / len(union)
    # len(intersection) , len(union) = 0, 0 => result = 1
    # 집합 A와 집합 B가 모두 공집합일 경우에는 나눗셈이 정의되지 않으니 따로 J(A, B) = 1로 정의한다.
    
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
    inter = []
    un = []
    
    for k in compare_2:
        if k in compare_1:
            inter.append(k)
    
    inter_dict_1 = {n:0 for n in inter}
    inter_dict_2 = {n:0 for n in inter}
    for l in inter:
        for m in compare_1:
            if m == l:
                inter_dict_1[l] += 1
        for o in compare_2:
            if o == l:
                inter_dict_2[l] += 1
    
    check = list(set(compare_1 + compare_2))
    for q in check:
        if q in inter:
            check.remove(q)
    numerator = []
    denominator = []
    for p in inter:
        for q in range(min(inter_dict_1[p], inter_dict_2[p])):
            numerator.append(p)
        for r in range(max(inter_dict_1[p], inter_dict_2[p])):
            denominator.append(p)
            
    denominator = denominator + check
    
    if len(numerator) == 0 or len(denominator) == 0:
        result =  1 * 65536
    else:
        result = int((len(numerator)/len(denominator))*65536)
        
    return result

print(solution("handshake","shake hands"))
        
                
                
            
            
    
    
        
        
    
    