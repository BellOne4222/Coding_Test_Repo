# 비내림차순이다. -> 수열이 같거나 커지는 순이다. 정렬 이후 시작 index를 기준으로 같은 index이거나 더 큰 index만 탐색한다.

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
temp = []

def dfs(start):
    if len(temp) == m:
        print(*temp)
        return
    remember_me = 0
    for i in range(start, n):
        if remember_me != nums[i]:
            temp.append(nums[i])
            remember_me = nums[i]
            dfs(i)
            temp.pop()

dfs(0)