def solution(s):
    stack = [] # 스택 사용
    for i in s: # 스택이 비면 i 넣고 다음 i와 stack의 마지막 값이 같으면 pop 처리
        
        if len(stack) == 0:
            stack.append(i)
            
        elif stack[-1] == i:
            stack.pop()
            
            
        else:
            stack.append(i)
    
    
    
    if len(stack) == 0: # 짝이 다지어져서 stack에 아무것도 없으면 1, 짝이 안지어져서 남아있다면 0 반환
        result = 1
    elif len(stack) > 0:
        result = 0
    
    return result