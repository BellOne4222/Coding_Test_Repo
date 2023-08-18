# 해시 테이블을 비우고 다시 만들고 넣는 과정이 반복되니까 시간초과가 뜨는거 같아서 해시 테이블에 전화번호들을 다 넣어 놓고 접두어를 한글자씩 넣으면서 해시 테이블에서 접두어가 같은게 있는지 확인하는 로직

def solution(phone_book):
    hash_table = {}
    result = True
    for i in phone_book:
        hash_table[i] = 1
    
    for j in phone_book:
        compare = ""
        for k in j:
            compare += k
            if compare in hash_table and compare != j:
                result = False
                return result
    return result
