# 1933 간단한 N의 약수

T = int(input())
nums = []
for i in range(1,T+1):
    if T % i == 0:
        nums.append(i)
str = ' '.join(map(str, nums)) # join을 사용하여 리스트를 문자열로 변환하고, map을 사용하여 안의 정수 값들을 문자열로 변환
print(str)