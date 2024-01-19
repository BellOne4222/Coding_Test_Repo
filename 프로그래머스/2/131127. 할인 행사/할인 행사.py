from collections import Counter

def solution(want, number, discount):
    result = 0
    
    # 정현이가 원하는 제품과 수량을 dictionary로 만듭니다.
    wants = dict(zip(want, number))  # {'banana': 3, 'apple': 2, 'rice': 2, 'pork': 2, 'pot': 1}
    
    # XYZ 마트에서 할인하는 제품을 10일씩 묶어서 확인합니다.
    for i in range(len(discount) - 10 + 1):
        discounts = Counter(discount[i:i+10])  # 현재 10일 동안의 할인 제품을 세어서 Counter 객체 생성
        discounts = dict(discounts)  # Counter 객체를 dictionary로 변환
        # {'chicken': 1, 'apple': 3, 'banana': 2, 'rice': 2, 'pork': 2}
        # {'apple': 3, 'banana': 2, 'rice': 2, 'pork': 2, 'pot': 1}
        # {'apple': 2, 'banana': 3, 'rice': 2, 'pork': 2, 'pot': 1}
        # {'banana': 3, 'rice': 2, 'apple': 2, 'pork': 2, 'pot': 1}
        # {'rice': 2, 'apple': 2, 'pork': 2, 'banana': 3, 'pot': 1}
        
        # 현재 10일 동안의 할인 제품이 정현이가 원하는 제품과 수량과 일치하는지 확인합니다.
        if discounts == wants:
            result += 1
    
    return result