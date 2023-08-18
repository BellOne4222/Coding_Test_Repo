def solution(n):
    tentotwo = str(bin(n))[2:] # bin을 사용해서 10진수를 2진수로 변환 후 앞에 0b가 붙기 때문에 슬라이싱으로 0b 제거한 2진수를 저장
    cnt_one = tentotwo.count("1") # 바꾼 2진수의 1의 개수 저장
    next_n = n+1 # 다음 n은 n보다 큰 자연수 이므로 1 더해서 변수에 저장
    result = 0 # 결과

    while True: # while 문 사용해서
    
        next_tentotwo = str(bin(next_n))[2:] # 위와 같은 방식으로 다음 n을 2진수로 변환하고 
        next_cnt_one = next_tentotwo.count("1") # 2진수의 1개수 저장
        
        if next_cnt_one == cnt_one: # 다음 n의 2진수와 원래 n의 2진수의 1의 개수를 비교해서 같으면 종료
            result = next_n
            break
        else:
            next_n += 1 # 같지 않으면 다음 n으로 이동해서 다시 반복문 실행
    
    
    return result # 결과 반환
        
        
        