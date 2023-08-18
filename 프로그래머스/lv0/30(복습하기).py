# 문자 반복 출력하기

def solution(my_string, n):
    my_string = list(my_string) # 리스트로 변환
    answer = []
    for i in my_string:
        answer.append([i*n]) #리스트 안에 [["문자열"],["문자열"]...] 으로 저장되므로 
    answer = sum(answer, []) # sum을 이용해서 리스트안에 리스트들을 다 합한다.
    answer = ''.join(answer) # join을 이용해서 안에있는 문자열들을 다 하나의 문자열로 합한다.
    return answer