# 2071 평균값 구하기

T = int(input())
for test_case in range(1, T + 1):
    li = list(map(int, input().split()))
    answer = round(sum(li)/len(li))
    print("#{} {}".format(test_case, answer))