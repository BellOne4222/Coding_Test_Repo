# 짝수는 싫어요

def solution(n):
    full = range(1,n+1) # 1~n까지의 배열 생성
    answer = [] 
    for i in full:
        if i % 2 != 0: 
            answer.append(i)  
    return answer