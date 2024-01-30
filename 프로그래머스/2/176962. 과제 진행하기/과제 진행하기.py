# 참고 : https://velog.io/@yeomja99/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%AC%B8%EC%A0%9C-%ED%92%80%EC%9D%B4%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EA%B3%BC%EC%A0%9C-%EC%A7%84%ED%96%89%ED%95%98%EA%B8%B0

def solution(plans):
    answer = []
    
    # plans 배열을 처리하여 시작 시각과 소요 시간을 정수로 변환
    for i in range(len(plans)):
        h, m = map(int, plans[i][1].split(':'))
        st = h * 60 + m
        plans[i][1] = st
        plans[i][2] = int(plans[i][2])

    # 시작 시각을 기준으로 정렬
    plans.sort(key=lambda x: x[1])
    
    stack = []
    for i in range(len(plans)):
        if i == len(plans) - 1:
            stack.append(plans[i])
            break

        sub, st, t = plans[i]
        nsub, nst, nt = plans[i+1]
        
        # 현재 과제의 끝나는 시각과 다음 과제의 시작 시각이 겹치지 않을 경우
        if st + t <= nst:
            answer.append(sub)
            temp_time = nst - (st + t)
            
            # 잠시 멈춰둔 과제가 있을 경우 처리
            while temp_time != 0 and stack:
                tsub, tst, tt = stack.pop()
                if temp_time >= tt:
                    answer.append(tsub)
                    temp_time -= tt
                else:
                    stack.append([tsub, tst, tt - temp_time])
                    temp_time = 0
            
        else:
            # 현재 과제의 소요 시간을 수정하여 스택에 추가
            plans[i][2] = t - (nst - st)
            stack.append(plans[i])

    # 스택에 남은 잠시 멈춰둔 과제들을 처리
    while stack:
        sub, st, tt = stack.pop()
        answer.append(sub)

    return answer