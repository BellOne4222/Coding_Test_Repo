# Bottom-Up : 반복문을 사용하여 작은 문제 부터 답을 도출

# 결과를 저장하기 위한 dp 테이블 초기화
d = [0] * 100

# 1, 2번째 피보나치 수는 1
d[1] = 1
d[2] = 1
n = 99

# 반복문으로 3~n까지 피보나치 수 구하기
for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n])

# setrecursionlimit()을 사용해 재귀 제한을 완화 시킬수 있다. sys.setrecursionlimit() -> 재귀 깊이 관련 오류 해결