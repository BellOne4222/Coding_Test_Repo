def solution(plans):

    plans = sorted(map(lambda x: [x[0], int(x[1][:2]) * 60 + int(x[1][3:]), int(x[2])], plans), key=lambda x: -x[1])
    answer = []
    while plans:
        x = plans.pop()
        for idx, val in enumerate(answer):
            if val[0] > x[1]:
                answer[idx][0] += x[2]
        answer.append([x[1] + x[2], x[0]])
    answer.sort()

    return list(map(lambda x: x[1], answer))

print(solution([["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]))

# 입력된 "plans"를 처리하여 시간 순서대로 정렬합니다. 각 계획은 [과목명, 시작 시간(분), 소요 시간] 형식의 리스트로 변환됩니다. 이때, 시작 시간을 분 단위로 변환하여 계산합니다. (예: "12:40" -> 12 * 60 + 40 = 760)
# 빈 리스트인 "answer"를 생성합니다.
# "plans"가 비어있을 때까지 다음을 반복합니다:
# "plans"에서 가장 늦게 시작하는 계획을 꺼내옵니다.
# "answer"에 있는 각 계획의 시작 시간과 비교하여 해당 시간 이후에 시작하는 계획이라면, 해당 계획의 시작 시간을 더하고 시간이 겹치는 경우를 처리합니다.
# 현재 계획을 "answer"에 추가합니다. [계획의 종료 시간, 과목명] 형식으로 저장됩니다.
# "answer"를 시간 순서대로 정렬합니다.
# "answer"에서 각 계획의 과목명만 추출하여 리스트로 변환합니다.
# 변환된 리스트를 반환합니다.