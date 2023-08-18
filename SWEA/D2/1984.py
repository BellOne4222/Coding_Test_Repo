# 1984 중간 평균값 구하기

T = int(input())

for test_case in range(1, T + 1):
    nums = list(map(int, input().split()))
    nums.remove(max(nums))
    nums.remove(min(nums))
    avg = sum(nums) / len(nums)
    print("#{} {}".format(test_case, round(avg)))