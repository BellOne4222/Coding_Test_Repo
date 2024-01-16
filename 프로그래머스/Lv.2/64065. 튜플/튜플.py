def solution(s):
    
    # 주어진 문자열 s는 튜플을 표현하는 집합을 나타내고 있습니다.

    # 문자열을 처리하기 위해 중괄호와 쉼표를 기준으로 나눠 리스트로 만들어줍니다.
    lst = sorted([s.split(',') for s in s[2:-2].split('},{')], key=len)

    # 결과를 저장할 빈 리스트를 만듭니다.
    result = []

    # 리스트를 순회하며 튜플을 구성하는 각 숫자를 결과 리스트에 추가합니다.
    for i in lst:
        for j in i:
            # 중복되지 않게 숫자를 추가합니다.
            if int(j) not in result:
                result.append(int(j))
                break

    # 결과 리스트를 출력합니다.
    return result