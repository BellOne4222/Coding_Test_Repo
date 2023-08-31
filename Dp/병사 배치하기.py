# 이것이 취업을 위한 코딩테스트다 p.380 병사 배치하기
# 부분 수열의 증가하는 최대 길이 알고리즘

n = 7
soldier = [15,11,4,8,5,2,4]

soldier.reverse()

dp = [1] * n

# 가장 긴 증가하는 부분 수열(LIS) 알고리즘 수행
for i in range(1,n):
    for j in range(0,i):
        if soldier[j] < soldier[i]:
            dp[i] = max(dp[i], dp[j]+1)

# 열외시켜야 하는 병사의 최소수
print(n - max(dp))