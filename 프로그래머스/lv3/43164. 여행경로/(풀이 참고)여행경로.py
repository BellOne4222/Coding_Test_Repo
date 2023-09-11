# 풀이 참고 : https://hi0seon.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%97%AC%ED%96%89%EA%B2%BD%EB%A1%9C-%ED%8C%8C%EC%9D%B4%EC%8D%AC-DFS

# dfs, defaultdict 사용


from collections import defaultdict

# 항공권 정보를 입력으로 받아 여행 경로를 찾는 함수
def solution(tickets):
    result = []  # 여행 경로를 저장할 리스트
    tickets.sort(key=lambda x: (x[1], x[0]))  # 항공권을 목적지를 기준으로 정렬, 목적지가 같다면 출발지를 기준으로 정렬
    airport_dict = defaultdict(list)  # 출발 공항을 키로 가지고 목적 공항 리스트를 값으로 갖는 딕셔너리 생성

    # 항공권 정보를 딕셔너리에 저장
    for [start, end] in tickets:
        airport_dict[start].append(end)

    # 출발 공항별 목적 공항 리스트를 내림차순으로 정렬
    for k in airport_dict.keys():
        airport_dict[k].sort(reverse=True)

    # 깊이 우선 탐색 함수 정의
    def DFS():
        path = ["ICN"]  # 경로를 저장할 스택, 초기값은 ICN 공항
        while path:
            start = path[-1]  # 현재 위치는 스택의 맨 위에 있는 공항
            if not airport_dict[start]:  # 현재 위치에서 더 이상 갈 수 있는 공항이 없으면
                result.append(path.pop())  # 경로에서 현재 위치를 제거하고 결과 리스트에 추가
            else:
                path.append(airport_dict[start].pop())  # 현재 위치에서 갈 수 있는 공항이 있으면 스택에 추가

    DFS()  # DFS 함수를 호출하여 여행 경로를 찾음
    return result[::-1]  # 결과 리스트를 역순으로 반환 (ICN부터 출발하는 경로)



print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))