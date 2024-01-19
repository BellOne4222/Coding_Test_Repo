# https://school.programmers.co.kr/questions/58068 참고

from itertools import product

users = [[40, 10000], [25, 10000]]
emoticons = [7000, 9000]

discount_rates = [10, 20, 30, 40]
result = []

# 가능한 이모티콘 할인율의 모든 조합을 생성
discount_cases = list(product(discount_rates, repeat=len(emoticons)))

# 모든 할인 조합에 대해 가입자 수와 판매액 계산
for discount_case in discount_cases:
    members = 0  # 가입자 수 초기화
    income = 0   # 판매액 초기화

    # 각 사용자에 대해 구매 여부 확인
    for required_discount, budget in users:
        purchased = 0

        # 각 이모티콘에 대해 사용자의 구매 여부 판단
        for i in range(len(emoticons)):
            if required_discount <= discount_case[i]:
                # 한 사용자의 구매액은 자신의 기준 할인율 이상 할인하는 이모티콘의 할인가
                purchased += emoticons[i] - emoticons[i] * discount_case[i] * 0.01
            
        if purchased >= budget:
            # 총 구매액이 사용자의 예산 이상이면, 구매하지 않고 플러스 가입자로 처리
            members += 1
        else:
            # 그렇지 않다면 이모티콘을 구매하므로 총 판매액에 합산
            income += purchased
        
    # 할인 조합별 총 가입자 수와 판매액을 배열에 저장
    result.append((members, income))
    # 	[(0, 0), (0, 0), (0, 6300.0), (0, 10800.0), (0, 0), (0, 0), (0, 6300.0), (0, 10800.0), (0, 4900.0), (0, 4900.0), (1, 0), (1, 5400.0), 
    # (0, 8400.0), (0, 8400.0), (1, 4200.0), (0, 19200.0)]
    
# 조합별로 가입자 수가 많은 순서대로, 가입자 수가 같으면 판매액이 많은 순서대로 정렬
answer = sorted(result, reverse=True, key=lambda x: (x[0], x[1]))
# [(1, 5400.0), (1, 4200.0), (1, 0), (0, 19200.0), (0, 10800.0), (0, 10800.0), (0, 8400.0), (0, 8400.0), (0, 6300.0), (0, 6300.0), (0, 4900.0), 
# (0, 4900.0), (0, 0), (0, 0), (0, 0), (0, 0)]

print(answer[0])