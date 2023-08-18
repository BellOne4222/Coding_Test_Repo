# 최댓값 만들기

def solution(numbers):
    numbers.sort() # 리스트 정렬
    numbers.reverse() # 리스트 뒤집기
    answer = numbers[0] * numbers[1]
    return answer