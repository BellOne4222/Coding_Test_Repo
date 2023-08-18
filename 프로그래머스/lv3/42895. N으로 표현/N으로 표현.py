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

