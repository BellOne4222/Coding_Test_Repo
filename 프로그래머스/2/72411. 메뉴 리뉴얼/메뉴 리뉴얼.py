from itertools import combinations
from collections import Counter

def solution(orders, course):    
    
    result = []  # 결과를 담을 리스트 초기화
    
    for num in course:  # 코스 요리 메뉴의 각 원소에 대해 반복
        combinationMenus = []  # 조합된 메뉴를 담을 리스트 초기화
        for order in orders:  # 주문들에 대해 반복
            for i in combinations(order, num):  # 각 주문에서 가능한 조합들을 생성
                combiMenu = ''.join(sorted(i))  # 조합된 메뉴를 알파벳 순으로 정렬하여 문자열로 변환
                combinationMenus.append(combiMenu)  # 조합된 메뉴를 리스트에 추가
        hotCombiMenu = Counter(combinationMenus).most_common()  # 가장 많이 주문된 조합 메뉴를 카운트하여 가져옴
        
        # hotCombiMenu의 예시
        # Counter({'AC': 4, 'CD': 3, 'CE': 3, 'DE': 3, 'BC': 2, 'BF': 2, 'BG': 2, 'CF': 2, 'CG': 2, 'FG': 2, 'AD': 2, 'AE': 2, 'AB': 1, 'AF': 1, 'AG': 1, 'AH': 1, 'CH': 1, 'DH': 1, 'EH': 1})
        # [('AC', 4), ('CD', 3), ('CE', 3), ('DE', 3), ('BC', 2), ('BF', 2), ('BG', 2), ('CF', 2), ('CG', 2), ('FG', 2), ('AD', 2), ('AE', 2), ('AB', 1), ('AF', 1), ('AG', 1), ('AH', 1), ('CH', 1), ('DH', 1), ('EH', 1)]
        
        for combi_menu, count in hotCombiMenu:  # 가장 많이 주문된 조합 메뉴들에 대해 반복
            if count > 1 and count == hotCombiMenu[0][1]:  # 주문 횟수가 1보다 크고, 가장 많이 주문된 횟수와 같은 경우
                result.append(combi_menu)  # 결과 리스트에 조합 메뉴 추가
        
    result.sort()  # 알파벳 순으로 정렬
    return result  # 결과 반환

# 작동 방식
# 코스 메뉴 반복: course 리스트에 지정된 각 코스 크기에 대해 함수는 반복문을 시작합니다.
# 조합 생성: 각 주문에 대해 모든 가능한 메뉴 조합을 생성합니다. 이는 itertools의 combinations 함수를 사용하여 수행됩니다.
# 조합 발생 횟수 카운트: 각 조합 메뉴의 발생 횟수를 카운트합니다.
# 가장 많이 주문된 조합 선택: Counter 객체의 most_common 메서드를 사용하여 가장 자주 주문된 조합을 식별합니다. 이는 조합 메뉴와 해당 카운트를 담은 튜플의 리스트를 반환합니다.
# 결과 필터링 및 추가: 함수는 두 번 이상 주문된 조합을 필터링하고, 가장 높은 카운트와 같은 카운트를 가진 조합을 결과에 추가합니다.
# 결과 정렬: 마지막으로, 결과가 알파벳 순으로 정렬되어 반환됩니다.