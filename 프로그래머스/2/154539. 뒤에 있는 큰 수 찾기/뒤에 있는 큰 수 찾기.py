from collections import deque

def solution(numbers):
    result = deque()
    stack = []

    for i in range(len(numbers)-1, -1, -1):
        current_number = numbers[i]

        while stack and stack[-1] <= current_number:
            stack.pop()

        if not stack:
            result.appendleft(-1)
        else:
            result.appendleft(stack[-1])

        stack.append(current_number)

    return list(result)