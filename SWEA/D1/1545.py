# 1545 거꾸로 출력해보아요

T = int(input())
nums = []
n = T
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for i in range(0, T+1):
    num = n - i
    nums.append(num)

str = ' '.join(map(str,nums))
print(str)