
def solution(n):
    tentothree = '' # 10진수에서 3진수로 바꾸기 위한 문자열
    while True: # 10진수를 3진수로 변환 : 3으로 나누고 몫을 최신화 시키면서 그때마다의 나머지를 tentothree에 더하면서 3진수 변환
        if n < 3: # 3 미만의 수는 변환 불가 하므로 1로 초기화
            tentothree = '1'
            break
        a = n % 3
        tentothree += str(a)
        n //= 3
        if n // 3 < 1: # 몫이 1보다 작아지면 종료
            tentothree += str(n)
            break

    notation = [] # 3진수를 뒤집기 위해서 배열에 넣기
    for i in tentothree:
        notation.append(i)
    
    threetoten = [] # 3진수를 10진수로 바꾸기 위해 거꾸로 뒤집은 3진수를 넣을 배열
    for k in reversed(notation):
        threetoten.append(k)
    
    answer = []
    for l in range(len(threetoten)): # 3진수를 10진수로 변환하기 위해 끝의 자리 부터 3의 거듭제곱을 0부터 1씩 늘려가며 각 자리 숫자에 곱해서 answer 배열에 저장
        b = int(threetoten[l]) * pow(3, l)
        answer.append(str(b))
        
    result = 0 # answer배열에 있는 숫자들을 모두 더해서 10진수 결과 반환
    for num in answer:
        result += int(num)
    
    return result
        
    

        
    
        
        
        
        
        