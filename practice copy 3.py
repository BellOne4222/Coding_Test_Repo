t = int(input())
for _ in range(t):
    n = int(input())
    grade = []
    for _ in range(n):
        grade.append(list(map(int, input().split())))
    
    grade.sort(key=lambda x: x[0])  
    
    cnt = 1
    min_y = grade[0][1]
    
    for i in range(1, n):
        if grade[i][1] > min_y:
            min_y = grade[i][1]
            cnt += 1
    
    print(cnt)