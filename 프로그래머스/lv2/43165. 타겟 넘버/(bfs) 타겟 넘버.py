# bfs 방식은 모든 경우의 수를 배열 안에 넣어놓고 배열을 반복문 돌려서 타겟값과 같은 값의 개수를 반환하였다.

def solution(numbers, target):
    result = 0
    sums_lst = [0] # 초기값을 위해 sums_lst안에 0 넣어서 배여ㅕㄹ 생성
    for num in numbers:
        sums = []
        for sm in sums_lst: # 숫자를 더하고 뺀 값을 sums에 저장
            sums.append(sm + num)
            sums.append(sm - num)
        sums_lst = sums # 더하고 빼는 모든 경우의 수를 sums_lst로 배열을 바꾸는 방식으로 저장

    for i in sums_lst:
        if i == target: # 타겟값과 같은 개수 추출
            result += 1
    return result