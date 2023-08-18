# dfs + 재귀 방식은 경우의 수를 늘려가며 수의 누적합이 target과 같을때 마다 result += 1하는 로직
# 누적합에 경우의 수를 인덱스로 한 numbers배열의 숫자를 더하고 빼주어 경우의 수 생성
# case_cnt == 탐색의 깊이

result = 0

def dfs(numbers, target, case_cnt, sm): # case_int : 경우의 수, sm = 수의 누적합
    global result
    if case_cnt == len(numbers):
        if sm == target:
            result += 1
        return result
    
    else:
        dfs(numbers, target, case_cnt+1, sm + numbers[case_cnt]) 
        dfs(numbers, target, case_cnt+1, sm - numbers[case_cnt])
    
def solution(numbers, target):
    dfs(numbers, target, 0, 0)
    return result
