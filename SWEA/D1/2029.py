# 2029 몫과 나머지 출력하기

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    nums = list(map(int, input().split()))
    print("#{} {} {}".format(test_case, nums[0]//nums[1], nums[0]%nums[1]))