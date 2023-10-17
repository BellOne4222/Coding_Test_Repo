# 참고 : https://omins.tistory.com/84
# 시간 복잡도 : O(N)


import sys

s = sys.stdin.readline().rstrip()
result = ''
stack = []

for i in s:  # 중위표기식의 각 원소에 대해
    if i.isalpha():  # 알파벳이면 result에 곧바로 추가
        result += i
    else:
        if i == '(':
            stack.append(i)
        elif i in ('+', '-'):  # 가장 우선순위가 낮은 연산자
            while stack and stack[-1] != '(':  # 여는 괄호를 만나면 멈추고
                result += stack.pop()  # 그렇지 않으면 stack 원소를 result에 추가
            stack.append(i)
        elif i in ('/', '*'):
            # 동일 우선순위 연산자는 먼저 나오는 연산자가 우선
            while stack and stack[-1] in ('/', '*'):
                result += stack.pop()
            stack.append(i)
        elif i == ')':  # 닫는 괄호를 만나면
            while stack and stack[-1] != '(':  # 괄호 내 모든 연산자를 result에 추가
                result += stack.pop()
            stack.pop()

# 알고리즘이 끝나고 스택에 원소가 있으면 모두 result에 추가
while stack:
    result += stack.pop()

print(result)