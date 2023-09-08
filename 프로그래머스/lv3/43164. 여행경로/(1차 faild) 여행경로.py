from collections import deque

def solution(tickets):
    # 도착지 기준으로 정렬하고, 같으면(경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 선택해야하기 때문에) 출발지 기준으로 정렬
    tickets.sort(key = lambda x:(x[1], x[0])) 
    
    # 노드 번호가 아니라 공항 이름으로 노드 이름이 나와있어서 트리 구조를 만들기 위해 dictionary 사용
    airport_dict = {}
    for i in range(len(tickets)):
        airport_dict[tickets[i][0]] = tickets[i][1]
    # 	{'JFK': 'HND', 'HND': 'IAD', 'ICN': 'JFK'}
    
    result = deque()
    
    # 처음 시작 위치는 ICN 이므로 ICN 먼저 넣어준다.
    path = ["ICN"]
    result.append("ICN")
    
    while True:
        if len(result) >= 2 and result[-2] == result[-1]:
            result.pop()
            break
        start = path[-1]
        if airport_dict[start] not in airport_dict:
            result.appendleft(airport_dict[start])
        else:
            result.appendleft(airport_dict[start])
            path.append(airport_dict[start])
    
    return result

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))