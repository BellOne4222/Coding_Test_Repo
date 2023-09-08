# 항공권 정보를 입력으로 받아 여행 경로를 찾는 함수
def solution(tickets):
    answer = []  # 가능한 여행 경로를 저장할 리스트

    # 각 항공권을 사용했는지 여부를 나타내는 리스트 초기화
    visited = [False] * len(tickets)

    # 깊이 우선 탐색 함수 정의
    def dfs(airport, path):
        # 경로의 길이가 항공권 개수보다 1 크다면 (모든 공항을 방문한 경우)
        if len(path) == len(tickets) + 1:
            answer.append(path)  # 가능한 경로를 결과 리스트에 추가
            return

        # 모든 항공권을 확인하면서 현재 공항에서 출발하는 항공권을 찾음
        for idx, ticket in enumerate(tickets):
            if airport == ticket[0] and not visited[idx]:
                visited[idx] = True  # 해당 항공권을 사용했음을 표시
                dfs(ticket[1], path + [ticket[1]])  # 다음 공항으로 이동하면서 경로에 추가
                visited[idx] = False  # 다른 경로로 탐색하기 위해 사용 여부 초기화

    dfs("ICN", ["ICN"])  # ICN 공항에서 출발하는 첫 번째 경로를 시작점으로 탐색

    answer.sort()  # 가능한 여행 경로를 사전순으로 정렬
    return answer[0]  # 가장 사전순으로 빠른 여행 경로를 반환