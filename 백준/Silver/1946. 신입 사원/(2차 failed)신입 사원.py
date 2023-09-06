import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    grade = [list(map(int, input().split())) for _ in range(n)]
    
    grade.sort(key=lambda x: x[0])  # x[0]을 오름차순, x[1]을 내림차순으로 정렬
    
    cnt = 1
    idx = 0
    min_y = grade[0][1]
    
    for i in range(1, n):
        if grade[i][1] < min_y:
            min_y = grade[i][1]
            cnt += 1
    
    print(cnt)
        
        
    