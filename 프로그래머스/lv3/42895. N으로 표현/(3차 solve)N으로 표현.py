# 2차 시도에서 실패하고 풀이 참고
# https://datacodingschool.tistory.com/212
# 문제는 즉, 1~8번까지 순회해서 만들어지는 수들의 집합 속에 number가 있는 최소 수를 찾아내기

def solution(N, number):
    minimum = -1

    # number가 N이면 반복 돌 필요없으므로 1반환
    if number == N: 
        return 1
    
    d = [set() for i in range(8)] # 결과 값들이 중복 되는게 많아서 set로 dp테이블을 만들어 중복을 제거
    for i in range(len(d)): # 미리 N을 i번 연속된 수를 dp테이블에 add로 넣어준다
        d[i].add(int(str(N)*(i+1)))
    
    # 8이후로는 -1로 반환하면 되므로 8까지 반복문 돌리기
    for i in range(1,8):
        # 0-i까지 반복
        for j in range(i):
            # N을 j개를 사용해서 만든 결과 값들 집합에서 반복
            for make1 in d[j]:
                # N을 i-j-1개를 사용해서 만든 결과 값들 집합에서 반복 
                for make2 in d[i-j-1]:
                    # 사칙연산 결과 값들을 dp테이블에 add로 저장
                    d[i].add(make1+make2)
                    d[i].add(make1-make2)
                    d[i].add(make1*make2)

                    # 나눗셈시 나누려는 수가 0이면 에러가 나므로 0이 아닐때만 dp테이블에 나눗셈 결과 추가
                    if make2 != 0:
                        d[i].add(make1//make2)
        # 찾는 number가 dp테이블에 있다면 dp테이블 인덱스 번호는 0부터 시작하므로 number가 있는 테이블의 인덱스 번호에 1 추가해서 가장 최소의 dp테이블 번호 반환하고 반복 종료
        if number in d[i]:
            minimum = i+1
            break
    
    return minimum
# [ SET x 8 ] 인 리스트를 만듭니다. 각각 N을 1개로 표현하는 수들의 집합, 2개로 표현하는 수들의 집합, ... 8개로 표현하는 수들의 집합이 저장됩니다.
# 8개의 SET에 개수만큼 N을 연달아 표현되는 수를 집어넣어줍니다.
# 숫자 N에 대해서 n개를 사용해서 표현한 수의 일반화 수식을 코드로 표현합니다.
# i에 대해서 1-8까지 순회합니다.
# j에 대해서 0-i까지 순회합니다.
# j개를 사용해서 만든 수들의 집합 s[j]를 다음과 같이 순회합니다.
# i-j-1을 사용해서 만든 수들의 집합 s[i-j-1]를 다음과 같이 순회합니다.
# make1(s[j] 순회 수)과 make2(s[i-j-1] 순회 수)를 사칙연산합니다. 나눗셈 시 make2는 0이 되면 안됩니다.
# 사칙연산한 결과 값을 집합 s[i]에 추가합니다.
# 만약 number가 s[i]에 존재한다면, 반복을 멈추고 i+1번을 반환합니다.
# 8번을 순회했음에도, number를 못찾는다면, -1을 반환합니다.

