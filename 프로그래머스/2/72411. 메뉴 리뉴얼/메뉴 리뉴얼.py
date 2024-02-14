from itertools import combinations
from collections import Counter

def solution(orders, course):    
    
    result = []
    
    for num in course:
        combinationMenus = []
        for order in orders:
            for i in combinations(order, num):
                combiMenu = ''.join(sorted(i))
                combinationMenus.append(combiMenu)
        hotCombiMenu = Counter(combinationMenus).most_common() # Counter({'AC': 4, 'CD': 3, 'CE': 3, 'DE': 3, 'BC': 2, 'BF': 2, 'BG': 2, 'CF': 2, 'CG': 2, 'FG': 2, 'AD': 2, 'AE': 2, 'AB': 1, 'AF': 1, 'AG': 1, 'AH': 1, 'CH': 1, 'DH': 1, 'EH': 1})
        # most_common() : [('AC', 4), ('CD', 3), ('CE', 3), ('DE', 3), ('BC', 2), ('BF', 2), ('BG', 2), ('CF', 2), ('CG', 2), ('FG', 2), ('AD', 2), ('AE', 2), ('AB', 1), ('AF', 1), ('AG', 1), ('AH', 1), ('CH', 1), ('DH', 1), ('EH', 1)]
        
        for combi_menu, count in hotCombiMenu:
            if count > 1 and count == hotCombiMenu[0][1]:
                result.append(combi_menu)
        
    result.sort()
    return result