# 10912. 외로운 문자

# 알파벳 소문자 만으로 이루어진 문자열이 주어진다.

# 이 문자열에서 같은 두 문자들을 짝짓고 남는 문자가 무엇인지 구하는 프로그램을 작성하라.

# 같은 문자를 여러 번 짝지어서는 안 된다.

 

# [입력]

# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

# 각 테스트 케이스의 첫 번째 줄에는 알파벳 소문자 만으로 이루어진 문자열이 주어진다.

# 이 문자열의 길이는 1이상 100이하이다.

 

# [출력]

# 각 테스트 케이스 마다 예제와 같은 형식으로 남는 문자를 사전 순서대로 출력한다.

# 만약 어떤 문자도 남지 않는다면 “Good”을 출력하도록 한다.

T = int(input())

for test_case in range(1, T+1):
    string = list(input())
    string.sort() 
    stack = []
    for i in range(len(string)): 
        if len(stack) == 0: # 스택에 아무것도 없으면 문자열의 원소 하나를 넣고
            stack.append(string[i])
        elif stack[-1] == string[i]: # 스택에 원소가 있으면 스택의 마지막 원소와 해당하는 위치의 문자열의 원소가 같으면 스택에서 pop(짝이 맞춰지면 pop)
            stack.pop()
        else:
            stack.append(string[i]) # 둘 다 아니라면 문자열의 해당하는 위치의 문자를 스택에 추가
    if len(stack) == 0: # 스택에 아무것도 없다면 good 반환, 있으면 남은 원소 join해서 문자열 반환
        ans = "Good"
    else:
        ans = ''.join(map(str, stack))
    
    print("#{} {}".format(test_case, ans))