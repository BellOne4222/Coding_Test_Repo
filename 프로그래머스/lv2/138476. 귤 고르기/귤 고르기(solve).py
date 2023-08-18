# 1차 코드에서 귤의 종류마다의 귤 개수를 파악하기 위해 count로 귤의 개수를 세서 귤 종류로 만든 딕셔너리에 개수를 추가
# 딕셔너리를 돌려서 귤 개수를 tangerines에 더하면서 k보다 같거나 크면 break해서 넘어 갈때마다 result(종류)에 1 추가 하는 방식으로 로직 구현
# 1차 코드에서는 시간 복잡도가 O(n^2)으로 시간초과 나서 실패했는데 2차 코드에서는 내장함수 counter를 사용해서 시간 복잡도를 O(nlogn)으로 줄여서 해결

from collections import Counter # counter는 리스트에서 중복된 데이터에서 각 원소가 몇 번씩 나오는지 저장된 객체를 반환한다.
# https://www.daleseo.com/python-collections-counter/ : 개념 참고

def solution(k, tangerine):
    tan_cnt = Counter(tangerine) # Counter({3: 2, 2: 2, 5: 2, 1: 1, 4: 1})
    tanger_dict = dict(sorted(tan_cnt.items(), key=lambda x: x[1], reverse=True)) # 귤의 종류별로 개수 딕셔너리로 생성하고, 개수 내림차 순으로 정렬
    
    tangerines = 0 # 총 귤 개수 반환
    result = 0 # 귤 종류 반환
    for tangerine, count in tanger_dict.items():
        if tangerines >= k: # 총 귤 개수가 k와 같거나 크면 종료
            break
        tangerines += count # 총 귤 개수에 귤 개수 더하기
        result += 1 # 종류가 바뀌면 result 1 추가
    
    return result
            
            
        
        
                        
        