import sys

input = sys.stdin.readline

n = int(input())

discussion = 0

discuss= []

for _ in range(n):
    discuss.append(list(map(int,input().split())))
    
# 회의가 일찍끝나는 순 정렬, 끝나는 시간이 같다면 회의 시작이 더 빠른 순으로 정렬
discuss.sort(key = lambda x:(x[1], x[0]))

ing = discuss[0][1]
discussion += 1

for i in range(1,n):
    if discuss[i][0] >= ing:
        discussion += 1
        ing = discuss[i][1]

print(discussion)


