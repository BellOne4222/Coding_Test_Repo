# 2007 패턴 마디의 길이

t = int(input())

for case in range(t):
    string = input()
    cnt = 1  # 패턴의 길이
    pattern = ""
    flag = False

    while True:
        pattern = string[:cnt]
        # print(pattern, cnt)
        if cnt == 10:
            break
        for i in range(cnt, len(string), cnt):
            if pattern != string[i:i + cnt]:
                break
            else:
                flag = True
                break

        if flag:
            break

        cnt += 1

    print("#%d" % (case+1), len(pattern))

    
# 처음에 pattern의 길이를 1로 했다가 점점 늘려가면서 pattern을 찾는다.

 

# 만약 입력받은 문자열이 'SAMSUNGSAMSUNGSAMSUNGSAMSUNGSA'이면

 

# 처음에 arr[0:1] = S와 arr[1:2] = A를 비교한다. 같지 않기 때문에 for문을 빠져나오고 pattern의 길이가 2가 된다.

 

# 두번째로 arr[0:2] = SA와 arr[2:4] = MS를 비교한다. 마찬가지로 같지 않기 때문에 for문을 빠져나오고 pattern의 길이가 3가 된다.

 

# 이렇게 계속 비교하다 pattern의 길이가 7이 되었을때, 즉 arr[0:7] = SAMSUNG 과 arr[7:14] = SAMSUNG 을 비교했을때, 같기 때문에 SAMSUNG이 패턴이 된다.

