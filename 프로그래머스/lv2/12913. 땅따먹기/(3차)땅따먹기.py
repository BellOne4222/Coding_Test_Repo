# DP - Bottom Up 방식
# 가능한 경우의 수 중 좋은 경우의 수만 남기는 greedy 알고리즘

def solution(land):
    # 높은 점수들을 반환 
    high_score_land = [0,0,0,0]
    for i in land:
        # land의 첫번째 원소의 이전행이 없으므로 시작을 0000에서 시작
        start = [0,0,0,0]
        for j in range(len(land[0])):
            # 이전 행은 한번 밟은 땅은 다시 못밟으므로 그 이전의 땅과 이후의 땅만 남겨서 새로운 배열로 생성
            previous_row = high_score_land[:j] +  high_score_land[j+1:]
            
            # 지금 행의 j인덱스의 값과 이전 행의 최댓값을 더한 것을 start[j] 에 저장
            start[j] = i[j] + max(previous_row)
        # 경우의 수마다 high_score_land를 저장한 start로 갱신
        high_score_land = start
        # print(high_score_land)
        # [1, 2, 3, 5]
        # [10, 11, 12, 11]
        # [16, 15, 13, 13]
    return max(high_score_land)
            