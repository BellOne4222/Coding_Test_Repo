def solution(numbers):
    answer = 0  # 결과값 초기화
    visit = [False]*len(numbers)  # 방문 여부를 나타내는 리스트 초기화

    # 주어진 숫자가 소수인지 확인하는 함수 정의
    def check(num):
        if num < 2:
            return False
        for i in range(2,num):
            if num % i == 0:
                return False
        return True
    
    myset = set()  # 중복 제거를 위한 집합 초기화

    # 깊이 우선 탐색을 통해 가능한 숫자 조합을 탐색하는 함수 정의
    def dfs(string, cnt):
        if cnt == len(numbers):  # 탐색이 끝났을 경우
            if string == '':  # 빈 문자열인 경우 제외
                return
            if int(string) in myset:  # 이미 탐색된 숫자인 경우 제외
                return
            if check(int(string)):  # 소수인 경우 결과값 증가 및 집합에 추가
                myset.add(int(string))
                nonlocal answer  # 외부 함수의 변수를 변경하기 위해 nonlocal 키워드 사용
                answer += 1
                return
        for i in range(len(numbers)):
            if visit[i]:  # 이미 방문한 경우 건너뜀
                continue
            visit[i] = True  # 방문 표시
            dfs(string,cnt+1)  # 현재 문자열로 탐색
            newstring = string + numbers[i]  # 새로운 문자열 생성
            dfs(newstring,cnt+1)  # 새로운 문자열로 탐색
            visit[i] = False  # 방문 표시 초기화
    
    dfs('',0)  # 깊이 우선 탐색 시작
    
    return answer  # 결과 반환