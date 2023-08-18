# startswith는 문자열이 특정문자로 시작하는지 여부를 알려준다
# 참고 : https://dpdpwl.tistory.com/119

def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True