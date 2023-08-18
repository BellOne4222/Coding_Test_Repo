# 리스트 생성하는 과정은 시간 복잡도가 O(n^2)에 count가 O(n)으로 시간 복잡도로 인해 시간초과로 테스트 케이스 6개 시간 초과가 떠서 실패...

def solution(k, tangerine):
    arr = list(set(tangerine))
    tan_dict = {i:0 for i in arr}
    for j in arr:
        tan_dict[j] = tangerine.count(j)
    
    tanger_dict = dict(sorted(tan_dict.items(), key=lambda x: x[1], reverse = True))
    
    tangerines = 0
    result = 0
    while True:
        for l in tanger_dict:
            tangerines += tanger_dict[l]
            result += 1
        if tangerines >= k:
            break
    return result