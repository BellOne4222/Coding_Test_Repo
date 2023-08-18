# 1970 쉬운 거스름돈

T = int(input())
for tc in range(1, T + 1):
    print('#{}'.format(tc))

    N = int(input())  # 32850
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    change = [0] * 8

    for i in range(8) : # 금액 종류
        if N // money[i] > 0: # 50000 지나쳐야 해 10000 1000 500 100 50-> 몫
            change[i] += N // money[i] # 3 2 1 3 1넣고
            N = N % money[i]   # 2850 850 350 50 0으로 다시 세팅

    print(*change)
    # [0, 3, 0, 2, 1, 3, 1, 0]