# 1986 지그재그 숫자

T = int(input())
for i in range(1, T+1):
    nums = list(map(int, input().split()))
    sum = 0
    for j in nums:
        for n in range(1, j+1):
            if n % 2 == 0:
                sum = sum - n
            elif n % 2 != 0:
                sum = sum + n
        print("#{} {}".format(i, sum))