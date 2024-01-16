def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x-1) + fibo(x-2)

print(fibo(4))

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

# 재귀적 풀이, Memoziation 사용
# Memoziation : 한 번 구한 결과를 메모리 공간에 메모해두고 같은 식을 다시 호출하면 메모한 결과를 그대로 가져오는 기법
# 한 번 구한 정보를 리스트에 저장하고 리스트에서 가져온다.
# 탑 다운 :  큰 문제를 해결하기 위해 작은 문제를 호출하는 기법

# 한 번 계산된 결과를 Memoziation하기 위한 리스트 초기화
d = [0] * 100

# 피보나치 함수를 재귀 함수로 구현(탑 다운)
def fibo(x):
    # 종료 조건
    if x == 1 or x == 2:
        return 1
    
    # d리스트에 값이 있으면(0이 아니면) = 이미 계산한 결과라면, 그대로 리스트에서 가져온다.
    if d[x] != 0:
        return d[x]

    # 없으면 점화식으로 결과 반환
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(99))

