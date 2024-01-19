from collections import deque

def solution(numbers):
    result = deque()
    stack = []  # 뒷 큰수를 찾기 위한 스택 초기화

    # 배열을 뒤에서부터 순회
    for i in range(len(numbers)-1, -1, -1):
        current_number = numbers[i]  # 현재 원소

        # 스택이 비어있지 않고, 스택의 맨 위에 있는 값이 현재 원소보다 작거나 같을 때까지 반복
        while stack and stack[-1] <= current_number:
            stack.pop()  # 스택의 맨 위 값이 현재 원소보다 작으면 제거

        # 스택이 비어있다면 결과에 -1 추가, 그렇지 않으면 스택의 맨 위 값 추가
        if not stack:
            result.appendleft(-1)
        else:
            result.appendleft(stack[-1])

        stack.append(current_number)  # 현재 원소를 스택에 추가

    return list(result)

# result: 뒷 큰수들을 저장하기 위한 데크(deque)를 초기화합니다.

# stack: 현재 원소보다 큰 수를 찾기 위한 스택을 초기화합니다.

# 배열을 뒤에서부터 순회하며 각 원소에 대한 뒷 큰수를 찾습니다.

# 현재 원소(current_number)와 스택을 사용하여 뒷 큰수를 찾는 과정을 수행합니다.

# 스택이 비어있지 않고, 스택의 맨 위에 있는 값(stack[-1])이 현재 원소보다 작거나 같을 때까지 반복합니다.

# 반복하면서 스택에서는 현재 원소보다 작은 값들을 제거합니다.

# 이렇게 함으로써 현재 원소보다 큰 수를 찾게 됩니다.

# 결과를 담는 데크(result)에 뒷 큰수를 추가합니다.

# 스택이 비어있다면 뒷 큰수가 없으므로 -1을 추가합니다.

# 그렇지 않으면 스택의 맨 위 값(현재 원소보다 큰 수)을 추가합니다.

# 현재 원소를 스택에 추가합니다.

# 스택에 현재 원소를 추가하여 이후의 원소들이 현재 원소를 뒷 큰수로 사용할 수 있도록 합니다.

# 뒤에서부터 순회하며 모든 원소에 대한 뒷 큰수를 찾은 후, 결과를 리스트로 변환하여 반환합니다.

# 이렇게 하면 각 원소에 대해 뒷 큰수를 효과적으로 찾아내고, 동일한 숫자가 여러 번 나타나는 경우에도 올바르게 처리할 수 있습니다.
