# 1966 숫자를 정렬하자

T = int(input())

for t in range(1, T+1) :
    N = int(input())
    num = list(map(int, input().split()))
    num.sort()
    li = ' '.join(map(str, num))
    print("#{} {}".format(t, li))