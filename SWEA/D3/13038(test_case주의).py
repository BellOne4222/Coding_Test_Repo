# 13038. 교환학생

# 세계 최고의 명문 대학교 삼성대학교에는 수많은 교환학생들이 존재한다. 삼성대학교는 연중무휴로 운영되지만, 교환학생들을 위한 수업은 특정 요일에만 진행된다. 이 정보는 7개의 정수 a1, a2, …, a7으로 표현되는데 (ai = 0 or ai = 1):

#   · 일요일에 교환학생을 위한 수업이 열리면 a1 = 1, 아니면 0
#   · 월요일에 교환학생을 위한 수업이 열리면 a2 = 1, 아니면 0
#   · …
#   · 토요일에 교환학생을 위한 수업이 열리면 a7 = 1, 아니면 0
 
#   수업이 어떠한 요일에도 열리지 않는 경우는 없다고 가정해도 된다.
#   당신은 삼성대학교에서 교환학생으로 n일 동안 수업을 들으려고 한다. 목표를 이루기 위해 삼성대학교에 지내야 하는 최소 일수를 출력하라.

# [입력]
#   첫 번째 줄에 테스트 케이스의 수 TC가 주어진다. 이후 TC개의 테스트 케이스가 새 줄로 구분되어 주어진다. 각 테스트 케이스는 다음과 같이 구성되었다.

#   · 첫 번째 줄에 정수 n이 주어진다. (1≤ n ≤105)
#   · 이후 7개의 정수 a1, a2, …, a7이 주어진다. (0 ≤ ai ≤ 1)

# [출력]
#   각 테스트 케이스마다 문제의 정답을 출력하라.

T = int(input())
 
for test_case in range(T):
    n = int(input())
    days = list(map(int, input().split()))
    cnt_lst = []
 
    for a in range(7):
        cnt2 = 0
        b = a
        cnt1 = 0
        while cnt2 < n:
            if days[b] == 1:
                cnt2+=1
            b+=1 # 일주일 도는용
            cnt1+=1
            if b == 7: # 연속된 날짜 제거용
                b=0
    
        cnt_lst.append(cnt1) # 모든 첫 개강일을 담아두는 배열을 만들고,그 배열을 for문을 통해 돌면서, 각 첫 개강일마다의 최소 일수를 계산했다.그리고 그 최소 일수들의 최솟값
    print("#{} {}".format(test_case+1,min(cnt_lst)))

# 연속된 날짜 테스트 케이스 
# 1 0 0 0 0 0 1
# 위 테스트 케이스는 일요일(a1)과 토요일(a7)에 강의가 열리는데, 이는
# 1 1 0 0 0 0 0
# 이 일요일(a1), 월요일(a2)에 강의가 열리는 테스트 케이스와 정답이 똑같이 나와야 한다.




