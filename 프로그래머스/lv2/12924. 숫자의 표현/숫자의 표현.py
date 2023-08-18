# 누적합 방식 사용, 시간 복잡도 : O(n^2)
# 시간 복잡도를 줄이려고 누적합 방식과 while 조건문도 n보다 작을 경우로 사용

def solution(n):
    result = 0 # 표현 방법 수
    for i in range(1, n+1):
        sum = 0
        j = i
        while sum < n: # i를 기준으로 j값을 1씩 증가 시키면서 sum에 j를 더하면서 sum == n이면 표현 횟수 증가 시키고 종료
            sum += j
            j += 1
            if sum == n:
                result += 1
                break
    return result
                    
    
    
    