def solution(s):
    
    # 주어진 문자열 s는 튜플을 표현하는 집합을 나타내고 있습니다.

    # # 맨 앞과 뒤의 {{, }} 를 지워줌
    # slice_s = s[2:-2]
    # # 문자열에서 숫자만 뺌
    # split_s = slice_s.split("},{")
    # split_s.sort(key=len)
    
    
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

# 위 코드는 다음과 같은 동작을 합니다:

# 주어진 문자열 s에서 중괄호와 쉼표를 기준으로 나누어 리스트 lst를 생성합니다.
# 리스트 lst를 길이 순으로 정렬합니다.
# 결과를 저장할 빈 리스트 result를 만듭니다.
# 리스트 lst를 순회하면서 각 숫자를 결과 리스트에 중복되지 않게 추가합니다.
# 최종 결과 리스트를 출력합니다.
# 따라서, s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"의 경우, 결과로 [2, 1, 3, 4]가 출력됩니다.