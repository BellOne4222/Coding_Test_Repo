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

# discount_rates에는 가능한 할인율의 종류가 나열되어 있습니다. 문제에서는 10%, 20%, 30%, 40% 중 하나를 설정할 수 있습니다.

# discount_cases에는 이모티콘 개별 할인율의 모든 조합이 들어있습니다. product 함수를 사용하여 할인율의 모든 조합을 만듭니다.

# for discount_case in discount_cases:를 통해 각 할인 조합에 대해 가입자수와 판매액을 계산합니다.

# for required_discount, budget in users:에서는 각 사용자의 구매 기준을 가져옵니다. required_discount는 해당 사용자가 원하는 할인율, budget는 해당 사용자의 예산입니다.

# for i in range(len(emoticons)):을 통해 각 이모티콘에 대해 사용자의 구매 여부를 판단합니다. 사용자의 할인 기준 이상이면 해당 이모티콘을 구매합니다.

# if purchased >= budget:에서는 사용자가 구매한 총 비용이 사용자의 예산 이상이면, 해당 사용자는 이모티콘을 구매하지 않고 플러스 가입자로 처리합니다.

# else:에서는 사용자가 구매한 총 비용을 계산하고, 이것을 총 판매액에 합산합니다.

# result.append((members, income))를 통해 해당 할인 조합에 대한 가입자수와 판매액을 저장합니다.

# answer = sorted(result, reverse=True, key=lambda x: (x[0], x[1]))를 사용하여 가입자수가 가장 많은 순으로, 가입자수가 같다면 판매액이 많은 순으로 정렬합니다.

# return answer[0]을 통해 최적의 할인 조합에 대한 가입자수와 판매액을 반환합니다.

# 이 코드는 가능한 모든 할인 조합을 고려하여 각 조합에 대해 가입자 수와 판매액을 계산하고, 그 중에서 최적의 조합을 찾아 반환하는 방식으로 동작합니다.