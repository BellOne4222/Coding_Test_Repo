# 새롭게 알게된 내장함수 bin(대상) : bin안에 있는 10진수 숫자를 2로 바꿔준다.
# n진수 → 10진수 : int(string, base)
# 10진수 → 2, 8, 16진수 : bin(), oct(), hex() 
# 위 방법은 앞에 0b가 붙기 때문에 [2:] 처리를 해줘야함

def solution(n, arr1, arr2): # arr1, arr2에 있는 10진수들을 2진수로 bin()을 사용하여 변환하여 각 번호의 리스트에 저장
    lst1 = [] 
    for i in arr1:
        a = bin(i) 
        a = a[2:] # 0b가 붙기 때문에 잘라서 변환
        if len(a) < n: # n보다 작으면 안맞기 때문에 자리수를 맞추기 위해 zfill로 n만큼 0을 추가(길이가 n보다 작을 경우)
            a = a.zfill(n)
            lst1.append(a)
        else:
            lst1.append(a)
    
    lst2 = [] # 위 방식과 같음
    for j in arr2:
        b = bin(j)
        b = b[2:]
        if len(b) < n:
            b = b.zfill(n)
            lst2.append(b)
        else:
            lst2.append(b)
    answer = ['' for _ in range(n)] # 빈 문자열 5개를 만들어 결과 배열 생성
    
    for k in range(n): # lst1 과 lst2를 둘다 돌면서 둘중 하나라도 1이면 정답 배열에 #추가하고 아니면 공백 추가해서 비밀지도 완성
        for l in range(n):
            if lst1[k][l] == "1" or lst2[k][l] == "1":
                answer[k] += "#"
            else:
                answer[k] += " "
    return answer
                
                
    
            
        
            