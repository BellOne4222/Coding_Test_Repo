t = int(input())
for _ in range(t):
    n = int(input())
    grade = []
    for _ in range(n):
        grade.append(list(map(int,input().split())))
    grade.sort(key = lambda x:x[0])
    standard_x = grade[0][0]
    standard_y = grade[0][1]
    cnt = 1
    for i in range(1,len(grade)):
        if grade[i][0] > standard_x and grade[i][1] > standard_y:
            continue
        else:
            if standard_y > grade[i][1]:
                standard_y = grade[i][1]
                cnt += 1
    print(cnt)