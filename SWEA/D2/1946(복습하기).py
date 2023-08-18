# 1946 간단한 압축 풀기

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    line = "" # 빈 문자열 생성
    for i in range(N):
        C,K = input().split() 
        K = int(K) # K는 문자열이므로 정수로 변환
        line += C * K  # 문자의 반복을 위해 곱해주고 line에 추가
    print("#{}".format(test_case))
    
    for i in range(len(line)): #line의 길이 만큼 반복
        if (i+1) % 10 == 0: # line이 10글자 다 채워지면
            print(line[i]) # 출력
        else:
            print(line[i], end = "")
    print()