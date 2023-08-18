
# 올바른 괄호 문자열 판별
def right_pls(s):
    stack = []
    
    # 나중에 들어온 괄호 쌍을 먼저 처리를 해줘야 하기 때문에 LIFO 성질을 이용하기 위해서 stack 사용
    # 나중에 들어온 괄호 쌍을 처리 해야 안에있는 먼저 들어온 괄호 쌍을 처리 가능
    # 짝이 없는 괄호를 stack에 저장
    # stack에 아무것도 없으면 올바른 괄호문자열, 있으면 올바르지 않은 괄호열로 처리
    for i in s:
        if stack and stack[-1] == "(" and i == ")":
            stack.pop()
        elif stack and stack[-1] == "{" and i == "}":
            stack.pop()
        elif stack and stack[-1] == "[" and i == "]":
            stack.pop()
        else:
            stack.append(i)
    
    return len(stack) == 0 # 스택이 비어있으면 올바른 괄호 문자열이므로

# 회전시키면서 문자열 확인
def solution(s):
    x_cnt = 0
    
    # 회전 하는 방식 아이디어를 고민하다가 deque 내장함수 rotate에 집중하여 구현을 해봤지만 실패하였습니다.
    # 그래서 다른 아이디어로 회전을 시키는게 아니라 슬라이싱으로 회전하는 효과를 줄 수 있게 구현
    # s = "[](){}" 이라고 했을 때, j = 1이라고 가정하고 왼쪽으로 회전하므로 왼쪽 두 개의 문자를 오른쪽으로 보내야 하는 것을
    # 슬라이싱으로 s[1:]를 앞으로 빼고, s[:1]을 뒤에 붙여서 j값의 변화에 따라 회전하는 로직으로 구현

    for j in range(len(s)): 
        if right_pls(s[j:]+s[:j]):
            x_cnt += 1 # 회전 할때마다 위의 올바른 문자열 판독 함수에서 stack이 빌때마다 x_cnt 1씩 증가해서 결과 반환
    
    return x_cnt
   