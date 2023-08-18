def solution(s):
    stack = []
    for c in s:
        if c == "(": # stack 자료형에 append
            stack.append(c)
        else: # c == ")"
            if stack: # stack에 뭔가 있다면
                stack.pop() # pop을 해서 stack이 비어있는데 pop을 하거나
            else: # stack에 비었는데 첫 문자가 ")"이라면 false
                return False
    if stack: # 마지막에 스택에 원소가 남아있는 경우 False, 비어있다면 True를 리턴하는 방법으로 문제를 해결
        return False
    return True

