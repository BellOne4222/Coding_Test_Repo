import copy

def solution(picks, minerals):
    answer = []

    # 피로도를 나타내는 2차원 배열
    tired = [[1, 1, 1],
             [5, 1, 1],
             [25, 5, 1]]

    # 각 광물을 인덱스로 표현하는 딕셔너리
    index = {'diamond': 0, 'iron': 1, 'stone': 2}

    # 광물을 캐는 재귀 함수
    def dfs(picks, minerals, value):
        # 종료 조건: 모든 곡괭이를 사용하거나 광물이 없을 때 결과값을 저장
        if sum(picks) == 0 or minerals == []:
            answer.append(value)

        # 현재 캘 광물의 다섯 개까지만 가져옴
        m = minerals[:5]

        can = []
        # 사용 가능한 곡괭이를 찾아서 리스트에 추가
        for idx, pick in enumerate(picks):
            if pick == 0:
                continue
            else:
                can.append(idx)

        # 각 곡괭이를 사용해 광물을 캐는 경우를 모두 탐색
        for c in can:
            v = 0
            # 현재 광물을 캐는 데 필요한 피로도를 계산
            for m_ in m:
                v += tired[c][index[m_]]

            # 곡괭이 사용 횟수를 갱신하고 재귀 호출
            temp = copy.deepcopy(picks)
            temp[c] -= 1
            dfs(temp, minerals[5:], value + v)

    # 초기값으로 시작
    dfs(picks, minerals, 0)

    # 결과 중에서 최솟값 반환
    return min(answer)