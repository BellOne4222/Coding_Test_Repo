# 3131. 100만 이하의 모든 소수

# 1 이상 100만(106) 이하의 모든 소수를 구하는 프로그램을 작성하시오.

# 참고로, 10 이하의 소수는 2, 3, 5, 7 이다.

# [입력]

# 이 문제의 입력은 없다.

# [출력]

# 1 이상 100만 이하의 소수를 공백을 사이에 두고 한 줄에 모두 출력한다.

# 내 풀이

n=1000000
a = [False,False] + [True]*(n-1)
primes=[]

for i in range(2,n+1):
    if a[i]:
        primes.append(i)
        for j in range(2*i, n+1, i):
            a[j] = False
ans = ' '.join(map(str, primes))
print(ans)


# 에라토스테네스의 체 알고리즘

import math

n = 1000000 # 2부터 1,000까지의 모든 수에 대하여 소수 판별
array = [True for i in range(n + 1)] # 처음엔 모든 수가 소수(True)인 것으로 초기화

# 에라토스테네스의 체 알고리즘 
for i in range(2, int(math.sqrt(n)) + 1): # 2부터 n의 제곱근까지의 모든 수를 확인하며
    if array[i] == True: # i가 소수인 경우 (남은 수인 경우)
        # i를 제외한 i의 모든 배수를 지우기
        j = 2 
        while i * j <= n:
            array[i * j] = False
            j += 1

# 모든 소수 출력
for i in range(2, n + 1):
    if array[i]:
        print(i, end=' ')