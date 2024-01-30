def solution(storey):
    stone = 0

    # storey가 10 미만인 경우
    if storey < 10:
        # storey가 10 미만이고 5 이하인 경우
        if storey <= 5:
            stone += storey # -1 돌을 storey 만큼 사용

        # storey가 10 미만이고 5초과 인경우
        else:
            stone += (11 - storey) # + 1 돌을 10이 될때까지 사용 후 -10 돌을 한번 사용


    # storey가 10 이상인 경우
    else:
        c = 1
        while True:
            cur_stone = 0

            # 10의 제곱수를 한자리씩 늘리면서 비교
            standard = 10 ** c

            # standard로 나눈 나머지
            rest = (storey % standard)

            # 나머지가 5이하이면 rest만큼 stone 사용 후 storey에서 stone 사용 수 * (standard ** c-1)만큼 차감
            if rest < (5 * pow(10, c-1)):
                cur_stone += (rest // pow(10, c-1))
                storey -= (cur_stone * pow(10, c-1))
                stone += cur_stone
            
            # 반례 : 75, 555
            # 나머지가 5이면 상위의 자리까지 고려
            # 5를 더했을 때 상위의 자리가 6이상이면 ((standard ** c) - rest) // (standard ** c-1) 만큼 돌 사용 후 storey에 stone 사용 수 * (standard ** c-1)만큼 추가  
            # 5를 더했을 때 상위의 자리가 6미만이면 rest만큼 stone 사용 후 storey에서 stone 사용 수 * (standard ** c-1)만큼 차감
            elif rest == (5 * pow(10, c-1)):
                a = (storey % pow(10, c+1)) + rest
                if a >= (6 * standard):
                    cur_stone += (pow(10, c) - rest) // pow(10, c-1)
                    storey += (cur_stone * pow(10, c-1))
                    stone += cur_stone
                else:
                    cur_stone += (rest // pow(10, c-1))
                    storey -= (cur_stone * pow(10, c-1))
                    stone += cur_stone

            # 나머지가 6이상이면 ((standard ** c) - rest) // (standard ** c-1) 만큼 돌 사용 후 storey에 stone 사용 수 * (standard ** c-1)만큼 추가  
            else:
                cur_stone += (pow(10, c) - rest) // pow(10, c-1)
                storey += (cur_stone * pow(10, c-1))
                stone += cur_stone

            c += 1 # standard 자리수 올리기

            # storey가 0이면 종료
            if storey == 0:
                break
    
    return stone
            