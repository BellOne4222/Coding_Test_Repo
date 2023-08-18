# 배열을 2배로 늘려서 하는 방법

def solution(elements):
    # 만들 수 있는 부분집합의 원소 최대 갯수
    ele_len = len(elements)
    
    # 원형을 구현하기 위해 리스트의 길이를 두배로 늘림
    tmp_list = elements + elements
    
    # 숫자를 저장하기 위해 집합 사용(중복 피하기)
    number = set()  
    answer = 0
    
    for i in range(1, ele_len + 1):
        for j in range(ele_len):
            # sum 함수를 이용해 부분집합을 더했을때의 숫자를 집합에 추가
            number.add(sum(tmp_list[j:j + i]))
            
    answer = len(number)
    return answer