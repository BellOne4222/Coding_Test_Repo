import sys

n,m = map(int, sys.stdin.readline().split())
result = []

def dfs(x):
    if len(result) == m:
        print(' '.join(map(str, result)))
        return
    
    # 기존에는 1부터 n까지 모든 숫자를 사용했지만 [2,1]과 같이 앞의숫자가 뒤의숫자보다 작은경우를 제외하기위해 x 변수를 사용해서 시작 위치설정
    for i in range(x,n+1):
        if i not in result:
            result.append(i)
            dfs(i+1) # 재귀함수를 호출할때는 i를 이용하여 자신의 다음숫자를 부르게된다.
            result.pop()
# 4,2
# dfs(1) -> result[1] -> dfs(2) -> result[1,2] -> dfs(3) -> len(result) == m print() -> 
# result.pop() -> result[1] -> result[1,3] 

dfs(1)