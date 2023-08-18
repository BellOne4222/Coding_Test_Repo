# 2068 최대수 구하기

T = int(input())
for i in range(1, T+1):
    num = list(map(int, input().split()))
    answer = max(num)
    print("#{} {}".format(i, answer))