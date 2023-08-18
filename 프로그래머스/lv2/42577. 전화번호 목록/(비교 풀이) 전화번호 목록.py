def solution(phone_book):
    phone_book.sort() 

    for i in range(len(phone_book) - 1):
        if phone_book[i] == phone_book[i + 1][:len(phone_book[i])]:
            # 현재 전화번호와 다음 전화번호를 지금 번호 길이 만큼 잘라서 비교해서 같으면 false 반환
            return False

    # 모든 전화 번호들의 접두사를 비교한 후 중복된 접두사가 없으면 True를 반환
    return True