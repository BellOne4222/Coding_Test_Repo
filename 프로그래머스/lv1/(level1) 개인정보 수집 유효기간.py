def solution(today, terms, privacies):
    
    today_year, today_month, today_day = today.split(".") # 오늘 날짜를 연, 월, 일로 쪼갬
    
    terms_dict = {} # 약관 종류와 유효기간을 딕셔너리로 저장
    for i in terms:
        term, expiration_date = i.split()
        terms_dict[term] = expiration_date
        
    result = []
    
    for i in range(len(privacies)):
        collect_date, terms_type = privacies[i].split() # 개인정보 수집 일자, 약관 종류
        collect_year, collect_month, collect_day = collect_date.split(".") # 개인정보 수집 일자를 연, 월, 일로 쪼갬
        
        # 판별 : 개인정보 수집 일자 + 약관 종류에 따른 유효기간 < 오늘 날짜이면 보관 가능하므로, 유효기간 < 오늘 날짜 - 개인정보 수집 일자가 만족 되면 보관 가능
        year_to_day = (int(today_year) - int(collect_year)) * 12 * 28 # 연, 월, 일 모두 일로 바꾸고 계산해서 월로 바꿔서 비교
        month_to_day = (int(today_month) - int(collect_month)) * 28
        day = (int(today_day) - int(collect_day))
        day_to_month = (int(year_to_day) + int(month_to_day) + int(day)) // 28
        
        if int(terms_dict[terms_type]) <= day_to_month:
            result.append(i+1)
        
    
    return result

# def solution(today, terms, privacies):
    
#     cal_today = list(today.split("."))
#     cal_today = ''.join(cal_today)
    
#     term_dict = {} # {'A': 6, 'B': 12, 'C': 3}
    
#     for i in range(len(terms)):
#         term_name, term = terms[i].split(" ")
#         term_dict[term_name] = int(term)
        
#     result = []
    
#     for j in range(len(privacies)):
#         deadline, term_name = privacies[j].split(" ")
        
#         deadline_lst = list(map(int,deadline.split(".")))
        
#         cal_m = deadline_lst[1] + term_dict[term_name]
        
#         if cal_m > 12:
#             cal_y = deadline_lst[0] + 1
#             deadline_lst[0] = cal_y
#             cal_m -= 12
        
#         cal_d = deadline_lst[2] - 1
#         if cal_d == 0:
#             cal_d = 28
#             cal_m -= 1
        
#         deadline_lst[1] = cal_m
#         deadline_lst[2] = cal_d
        
        
        
#         compare = ''
#         for k in range(len(deadline_lst)):
            
#             into = str(deadline_lst[k])
#             if len(into) == 1:
#                 zero_compare = '0'
#                 zero_compare += into
#                 compare += zero_compare
#             else:
#                 compare += into
        
#         if int(cal_today) > int(compare):
#             result.append(j+1)
        
#     return result
            
        
        
        
        
        
        
            
        
        