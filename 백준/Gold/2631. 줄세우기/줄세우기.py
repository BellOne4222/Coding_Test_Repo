import sys


n = int(sys.stdin.readline())

dp_table = [1] * (n+1)
nums = [0]
for i in range(n):
    nums.append(int(sys.stdin.readline()))

#가장 긴 증가하는 수열 찾기 
for i in range(1,n+1):
    for j in range(1,i):
        if nums[j] < nums[i]:
            dp_table[i]=max(dp_table[i],dp_table[j]+1)

#n- 긴 증가하는 부분수열의 길이 
print(n-max(dp_table))