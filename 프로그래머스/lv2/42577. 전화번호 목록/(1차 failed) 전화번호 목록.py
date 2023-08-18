# 효율성 테스트 3,4번 시간 초과 실패..

from collections import deque

def solution(phone_book):
    phone_book.sort() # ['119', '1195524421', '97674223']
    phone_book = deque(phone_book)
    hash_table = {}
    result = True
    
    # 덱 사용해서 전화번호 배열에서 가장 왼쪽 꺼 빼고, 뺀 전화번호와 길이가 같게 나머지 전화번호들 슬라이싱 해서 해시 테이블에 넣어서 만들어주고 접두사랑 같은게 있는지 in으로 확인해서 있으면 false, 없으면 true 반환
    for j in range(len(phone_book)):
        compare = phone_book.popleft()
        for i in phone_book:
            hash_table[i[:len(compare)]] = 1
        if compare in hash_table:
            result = False
            return result
        else:
            hash_table = {} # 중복된 접두사가 없으면 테이블 초기화
            
    return result