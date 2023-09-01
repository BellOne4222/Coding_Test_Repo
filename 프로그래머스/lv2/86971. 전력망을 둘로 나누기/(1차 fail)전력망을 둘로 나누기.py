# 각 노드마다 연결 된 노드의 개수를 파악하고, 공통적으로 가지고 있는 노드의 개수를 최빈값을 찾아서 각 노드마다 빼주어서 공통 보유 노드를 없애고 남은 노드의 합을 반환
# 예제 테스트 케이스는 다 통과했지만 뒤의 테스트 케이스는 1개 빼고 다 실패...
# 완탐이라서 알고리즘 안쓰고 풀어보려고 시도 했는데 트리 이므로 dfs or bfs 고민

from collections import Counter

def solution(n, wires):
    n_dict = {i:0 for i in range(1,n+1)}
    for j in range(len(wires)):
        n_dict[wires[j][0]] += 1
    
    n_lst = list(n_dict)
    # 	{1: 1, 2: 1, 3: 1, 4: 3, 5: 0, 6: 0, 7: 2, 8: 0, 9: 0}
    
    for k in n_lst:
        if n_dict[k] == 0:
            del n_dict[k]
    # 	{1: 1, 2: 1, 3: 1, 4: 3, 7: 2}
    
    m_lst = list(n_dict) 
    # 	[1, 2, 3, 4, 7]
    
    tower_lst = list(n_dict.values())
    
    common = Counter(tower_lst)
    
    m_common = common.most_common(1)
    
    most = m_common[0][0] # 1
    
    for l in m_lst:
        n_dict[l] -= most
    # [0, 0, 0, 2, 1]
    result = sum(list(n_dict.values()))
    
    return result
    
# 테스트 1 〉	실패 (0.06ms, 10.2MB)
# 테스트 2 〉	실패 (0.06ms, 10.1MB)
# 테스트 3 〉	실패 (0.07ms, 10.2MB)
# 테스트 4 〉	실패 (0.06ms, 10.2MB)
# 테스트 5 〉	실패 (0.09ms, 10.4MB)
# 테스트 6 〉	통과 (0.03ms, 10.1MB)
# 테스트 7 〉	실패 (0.04ms, 10.1MB)
# 테스트 8 〉	실패 (0.06ms, 10.2MB)
# 테스트 9 〉	실패 (0.06ms, 10.2MB)
# 테스트 10 〉	실패 (0.09ms, 10.2MB)
# 테스트 11 〉	실패 (0.06ms, 10.2MB)
# 테스트 12 〉	실패 (0.06ms, 10.1MB)
# 테스트 13 〉	실패 (0.10ms, 10.2MB)