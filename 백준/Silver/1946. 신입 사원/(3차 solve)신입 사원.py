# 정렬 사용
# 시도 끝에 서류 점수 순으로 정렬 하고 나서 면접 점수만 비교하면 된다는 사실을 알게되어서 서류 점수가 가장 높은 사원의 면접 점수를 최소로 설정하고, 그보다 작은 값이 반복문을 돌면서 있으면 그걸로 최솟값 설정해서 cnt +=1 하는 방식으로 solve

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    grade = [list(map(int, input().split())) for _ in range(n)]
    
    grade.sort(key=lambda x: x[0])  
    
    cnt = 1
    idx = 0
    min_y = grade[0][1]
    
    for i in range(1, n):
        if grade[i][1] < min_y:
            min_y = grade[i][1]
            cnt += 1
    
    print(cnt)
        
        
    