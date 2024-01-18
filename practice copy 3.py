# 입력값 〉	[10, 1, 10, 2, 10, 3, 10, 10, 10, 11, 11, 11, 12]
# 기댓값 〉	[11, 10, 11, 10, 11, 10, 11, 11, 11, 12, 12, 12, -1]


from collections import deque

result = deque()
stack = []

numbers = [10, 1, 10, 2, 10, 3, 10, 10, 10, 11, 11, 11, 12]

for i in range(len(numbers)-1, -1, -1):
    current_number = numbers[i]

    while stack and stack[-1] <= current_number:
        stack.pop()

    if not stack:
        result.appendleft(-1)
    else:
        result.appendleft(stack[-1])

    stack.append(current_number)


print(result)