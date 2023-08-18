def solution(s):
    result = "" # 결과 받을 문자열
    check = "" # 영어를 숫자로 바꾸기 위해 받을 문자열
    alpha_dict = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5","six":"6","seven":"7","eight":"8","nine":"9"}

    for i in s: 
        if i.isalpha(): # 문자열 s를 돌면서 i가 영어일 경우
            check += i # 확인하기 위해 check에 i 추가
            if check in alpha_dict: # 알파벳이 모여 숫자 영단어가 완성되는지 확인
                result += alpha_dict[check] # 만들어지면 결과에 바꾼 숫자 추가
                check = "" # 확인 한 문자열 초기화
        else:
            result += i # 영어가 아니라 숫자라면 결과에 그대로 추가
    
    return int(result) # 문자열이므로 정수로 바꾸어 결과반환
                
            
                
            
            
            
        
    