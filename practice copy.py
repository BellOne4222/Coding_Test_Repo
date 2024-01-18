from collections import deque

# 아래 반례 해결 실패
# 입력값 〉	[10, 1, 10, 2, 10, 3, 10, 10, 10, 11, 11, 11, 12]
# 기댓값 〉	[11, 10, 11, 10, 11, 10, 11, 11, 11, 12, 12, 12, -1]
# 결괏값 > [12, 10, 12, 10, 12, 10, 12, 12, 11, 12, 12, 12, -1]

def solution(numbers):
    # 결과를 담을 deque 생성
    result = deque()

    # 맨 마지막 원소에 대한 뒷 큰수는 항상 -1이므로 먼저 deque에 추가
    result.appendleft(-1)

    # 이전 순회에서의 현재 원소와 그보다 큰 수 중 가장 큰 값을 저장할 변수 초기화
    prev_num = numbers[len(numbers) - 1]
    prev_max_num = -1

    # 배열의 끝에서부터 역순으로 순회
    for i in reversed(range(len(numbers) - 1)):
        # 현재 원소보다 이전 원소가 크다면
        if prev_num > numbers[i]:
            # 결과 deque에 현재 원소보다 큰 수 추가
            result.appendleft(prev_num)
            # 현재 원소가 이전 순회에서의 가장 큰 수보다 크다면 업데이트
            if prev_max_num < prev_num:
                prev_max_num = prev_num
        
        elif numbers[i] == numbers[i+1]:
            result.appendleft(result[0])
            prev_max_num = result[0]

        else:
            # 현재 원소보다 이전 원소가 작다면
            if numbers[i] > prev_max_num:
                # 결과 deque에 -1 추가
                result.appendleft(-1)
                # 현재 원소가 이전 순회에서의 가장 큰 수보다 크면 업데이트
                prev_max_num = numbers[i]
            else:
                # 현재 원소보다 큰 수가 존재한다면 결과 deque에 추가
                result.appendleft(prev_max_num)

        # 이전 순회에서의 현재 원소를 업데이트
        prev_num = numbers[i]
    
    # deque를 list로 변환하여 결과 반환
    result = list(result)
    
    return result

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