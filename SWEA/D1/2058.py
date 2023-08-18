# 2058 자릿수 더하기

T = str(input())
li = list(T)
nums = []
for i in li:
    nums.append(int(i))
sum = 0
for num in nums:
    sum += num
print(sum)