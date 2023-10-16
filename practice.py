# 1.

def solution(books, target):
    power = 0 # 들인 힘을 받는 변수

    for i in range(len(target)):
        book = target[i]
        find = 0
        idx = 0
        while True:
            if books[idx] == book:
                books.insert(0, carry)
                carry = books.remove(books[idx])
                power += find
                break
            else:
                idx += 1
                find += 1
    
    return power

print(solution([3,1,2],[1,3,2]))