# 참고 : https://omins.tistory.com/84
# 시간 복잡도 : O(N)


import sys

# 중위 표기법 수식을 입력으로 받음
s = sys.stdin.readline().rstrip()

# 결과를 저장할 문자열
result = ''

# 연산자를 저장할 스택
stack = []

for i in s:  # 중위 표기식의 각 원소에 대해
    if i.isalpha():  # 알파벳(피연산자)이면 result에 곧바로 추가
        result += i
    else:
        if i == '(':  # 여는 괄호를 만나면 스택에 추가
            stack.append(i)
        elif i in ('+', '-'):  # 가장 낮은 우선순위의 연산자
            while stack and stack[-1] != '(':  # 여는 괄호를 만날 때까지
                result += stack.pop()  # 스택의 연산자를 result에 추가
            stack.append(i)
        elif i in ('/', '*'):  # 동일 우선순위의 연산자는 먼저 나온 연산자가 우선
            while stack and stack[-1] in ('/', '*'):
                result += stack.pop()
            stack.append(i)
        elif i == ')':  # 닫는 괄호를 만나면
            while stack and stack[-1] != '(':  # 여는 괄호를 만날 때까지
                result += stack.pop()  # 스택의 연산자를 result에 추가
            stack.pop()

# 알고리즘이 끝나고 스택에 남아있는 연산자들을 모두 result에 추가
while stack:
    result += stack.pop()

# 후위 표기법으로 변환된 수식 출력
print(result)