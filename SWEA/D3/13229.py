# 13229. 일요일

# 오늘의 요일을 나타내는 문자열 S가 주어진다. S는 “MON”(월), “TUE”(화), “WED”(수), “THU”(목), “FRI”(금), “SAT”(토), “SUN”(일) 중 하나이다.

# 다음 (즉, 내일 이후의 가장 빠른) 일요일까지는 며칠 남았을까?
 

# [입력]

# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

# 각 테스트 케이스는 하나의 줄로 이루어진다. 각 줄에는 문자열 S가 주어진다.
 

# [출력]

# 각 테스트 케이스마다, 다음 일요일까지 며칠 남았는지를 한 줄에 하나씩 출력한다.

T = int(input())
days = {"MON" : 1, "TUE" : 2 , "WED" : 3 , "THU" : 4 , "FRI" : 5 , "SAT" : 6 , "SUN" : 7 } # 요일 별로 숫자 딕셔너리에 저장

for test_case in range(1, T+1):
    day = input()
    ans = days["SUN"] - days[day]
    if day == "SUN": # 일요일이면 7 반환
        ans = 7

    print("#{} {}".format(test_case, ans))

    
    
