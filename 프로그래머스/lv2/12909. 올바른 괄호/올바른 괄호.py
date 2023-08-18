def solution(s):
    stack = []
    for i in s:
        if s[0] == ")": # s의 처음이 닫는 괄호이면 올바른 괄호가 아니므로 false 반환
            return False
        if len(stack) == 0: # 스택에 아무것도 없으면 괄호 하나를 추가하고
            stack.append(i)
        elif i == ")": # 닫는 괄호가 나오면 스택에서 여는 괄호 하나 삭제
            stack.pop()
        else: # 여는 괄호이면 스택에 추가
            stack.append(i)
    
    if len(stack) > 0: # 스택에 아무것도 없으면 올바른 괄호 이므로 true, 스택에 남는 괄호가 있으면 올바른 괄호가 아니므로 false 반환
        return False
    elif len(stack) == 0:
        return True
        
    