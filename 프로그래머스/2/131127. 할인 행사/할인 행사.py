from collections import Counter

def solution(want, number, discount):
    
    result = 0
    
    wants = dict(zip(want, number)) # {'banana': 3, 'apple': 2, 'rice': 2, 'pork': 2, 'pot': 1}
    
    for i in range(len(discount) - 10 + 1):
        discounts = Counter(discount[i:i+10])
        discounts = dict(discounts)
        
        if discounts == wants:
            result += 1
    
    return result