# 중앙값 구하기

def solution(array):
    array.sort()
    middle = int(len(array)/2)
    answer = array[middle]
    return answer