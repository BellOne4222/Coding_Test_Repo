import sys


N = int(input())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()
ans = 0

for i in range(N):
    tmp = nums[:i] + nums[i + 1:]
    l_idx, r_idx = 0, len(tmp) - 1
    while l_idx < r_idx:
        t = tmp[l_idx] + tmp[r_idx]
        if t == nums[i]:
            ans += 1
            break
        if t < nums[i]:
            l_idx += 1 # t 를 증가시켜야 하므로 l_idx 증가
        else:
            r_idx -= 1 # t 를 감소시켜야 하므로 r_idx 감소
        
print(ans)