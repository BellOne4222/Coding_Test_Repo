def solution(s):
    zero_count = 0 # 0의 개수를 받는 변수
    change_count = 0 # 이진 변환 횟수를 받는 변수
    while True: 
        zero_count += s.count("0") # 0의 개수를 변수에 저장
        s = s.replace("0",'') # 0은 공백으로 바꿔서 없앰
        ten_to_two = len(s) # 10진수를 2진수로 바꿀 숫자는 0을 없앤 s의 길이
        change_count += 1 # 바꿀 때 마다 횟수 증가
        s = bin(ten_to_two)[2:] # bin을 사용했으므로 앞에 붙은 0b 제거하고 출력
        if s == "1": # 이진 변환 후 1이 될 때까지 반복하고 1이면 종료
            break
        
        
    return [change_count, zero_count]  # 이진변환 횟수, 0의 개수 누적 합 반환
    
            
            
    