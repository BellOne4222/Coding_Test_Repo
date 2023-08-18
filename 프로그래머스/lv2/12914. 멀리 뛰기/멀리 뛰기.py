# DP 사용
# Bottom-up 방식 (for loop 반복문 사용, 아래부터 위로 올려서 계산, basecase를 필두로 밑에서 부터 위로 올라가는 방식)

memo = {0:0, 1:1, 2:2} # 메모리 사용
def solution(n):
    for i in range(3, n+1):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n] % 1234567