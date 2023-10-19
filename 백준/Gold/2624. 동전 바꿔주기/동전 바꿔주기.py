import sys
input = sys.stdin.readline

if __name__ == '__main__':
    T = int(input()) # 지폐의 금액
    K = int(input()) # 동전의 가지 수 
    coins = [] # 동전 정보
    dp = [0] * (T+1) # dp[n] : n 금액에 대한 동전 교환 방법의 가지 수 
    dp[0] = 1 # 0원은 아무 동전도 사용하지 않는 경우가 하나 있으므로 1로 초기화 

    for _ in range(K):
        p, n = map(int, input().split())
        coins.append((p, n))

    for coin, cnt in coins:
        for money in range(T, 0, -1): # T원부터 1원까지 내려가며 진행 
            for i in range(1, cnt+1): # 현재 동전 coin의 개수만큼 for문 진행 
                if money - coin * i >= 0: # 0원 이상인 경우
                    dp[money] += dp[money - coin * i]

    print(dp[T])