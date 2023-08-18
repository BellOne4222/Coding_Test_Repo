# 2070 큰놈 작은놈 같은놈

T = int(input())
for test_case in range(1, T + 1):
    li = list(map(int,input().split()))
    if li[0] >li[1]:
        result = ">" # result 사용
    elif li[0] == li[1]:
        result = "="
    elif li[0] < li[1]:
        result = "<"
    print("#{} {}".format(test_case, result))
