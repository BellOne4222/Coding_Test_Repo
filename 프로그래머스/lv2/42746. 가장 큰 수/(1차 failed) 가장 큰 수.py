# 1. 숫자의 맨 앞자리 수만 비교해서, 정렬을 해주고 앞자리가 같은 것을 처리하는 방법이 이 문제의 key라고 생각해서 비교를 하려면 자릿수를 같게 해줘야 겠다라는 생각 때문에 원소는 1000까지 이므로 4자리 까지 ljust를 사용해서 0으로 채워줘서 비교
# 예제 테스트 케이스는 해결 됐지만 뒤의 테스트 케이스에서 33.3점으로 실패... 3과 30은 0으로 채웠을 때, 둘 다 3000이므로 비교 불가 하다는 문제 발생
# 질문하기에서 [1, 10, 100, 1000, 818, 81, 898, 89, 0, 0] => 89/898/818/81/1/10/100/1000/0/0 => "8989881881110100100000" 반례 참고



def solution(numbers):
    numbers_str = list(map(str, numbers))
    
    nums_dict = {i:0 for i in numbers_str}
    
    change_lst = [] 
    for k in range(len(numbers)):
        change_lst.append([numbers_str[k].ljust(4,'0'),numbers_str[k]]) 
    
    change_lst.sort(key = lambda x:x[0], reverse = True)
    # [['6000', '6'], ['2000', '2'], ['1000', '10']]
    # [['9000', '9'], ['5000', '5'], ['3400', '34'], ['3000', '3'], ['3000', '30']]
    
    result = ''
    
    for l in range(len(numbers)):
        result += change_lst[l][1]
    
    return result