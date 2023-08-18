def solution(dartResult):
    num = ''
    answers = []
    for i in dartResult:
        if i.isnumeric(): # isnumeric() : 숫자로만 이루어진 문자열인지 판별 함수
            num += i # 문자열에 추가하는 방법으로 두자리 숫자도 해결
        elif i == "S":
            score = pow(int(num), 1)
            answers.append(score)
            num = ''
        elif i == "D":
            score = pow(int(num), 2)
            answers.append(score)
            num = ''
        elif i == "T":
            score = pow(int(num), 3)
            answers.append(score)
            num = ''
        elif i == "*":
            if len(answers) >= 2:
                answers[-2] *= 2
                answers[-1] *= 2
            else:
                answers[-1] *= 2
        elif i == "#":
                answers[-1] *= -1
        
    answer = sum(answers)
    return answer

            
            
        
            
    
    
        
                
                    
                
                
            