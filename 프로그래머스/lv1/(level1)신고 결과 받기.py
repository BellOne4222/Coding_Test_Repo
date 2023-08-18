def solution(id_list, reports, k):
    # 유저가 누구누구에 의해서 신고를 당했는지 딕셔너리로 반환
    reported_by_someone = {user_id:set() for user_id in id_list} # 같은 이용자에 대한 중복된 신고는 1개로 처리 되므로 set을 사용해서 중복 처리 
    for report in reports:
        user, report_to = report.split()
        reported_by_someone[report_to].add(user) # 각 사용자에 대해 사용자가 신고를 당한 신고자를 추가
    # {'muzi': {'apeach'}, 'frodo': {'apeach', 'muzi'}, 'apeach': set(), 'neo': {'frodo', 'muzi'}}
    # k번 이상 유저가 한 신고가 몇 번 접수됐는지 딕셔너리로 반환
    receive = {user_id:0 for user_id in id_list} # 0으로 key 값 설정해서 신고 접수 횟수를 받는 딕셔너리 생성
    for user_id in id_list: 
        if len(reported_by_someone[user_id]) >= k: # k번 이상 신고 접수를 받으면 정지
            for someone in reported_by_someone[user_id]: # 신고를 한 횟수 만큼 딕셔너리에 1씩 증가
                receive[someone] += 1  
    # {'muzi': 2, 'frodo': 1, 'apeach': 1, 'neo': 0}
    
    # 메일 받은 횟수 반환
    mail = [receive[user_id] for user_id in id_list] # 처리 결과 메일 받은 횟수 반환
    return mail

        
