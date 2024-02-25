# 3.
# RESERVATION 테이블은 회의실 예약 요청 정보를 담고 있는 테이블 입니다. RESERVATION 테이블은 다음과 같이 구성되어 있습니다. ID, USER_ID, START_TIME, END_TIME는 각각 예약 요청의 ID, 예약한 유저의 ID, 회의실 예약이 시작되는 시각, 회의실 예약이 끝나는 시각을 나타냅니다.
# 문제
# 회의실 예약 요청 정보를 통해 어떤 요청이 확정되었느지 알아보려고 합니다. 
# 예약 요청은 다음과 같이 처리 됩니다.
# 1. 요청된 회의실 이용 시간이 먼저 요청된 모든 예약들의 이용시간과 겹치지 않는다면 예약이 확정됩니다.
# 2. 먼저 끝나는 회의의 종료 시작과 다음 회의의 시작 시간이 같다면 두 이용 시간은 겹치지 않습니다.
# 3. 예약 요청 ID가 작을 수록 먼저 요청되었음을 의미합니다.
# 4. 확정되지 않은 예약 요청도 이후 발생하는 요청의 확정 여부에 영향을 줍니다.
# 예약이 확정된 요청의 ID와 회의실 이용 시작 시간, 종료 시간을 조회하는 SQL문을 작성해주세요.
# 결과는 회의실 이용 시작 시간을 기준으로 오름차순으로 정렬해주세요.

# SELECT ID, START_TIME, END_TIME 
# FROM (
#     SELECT 
#         ID, 
#         START_TIME, 
#         END_TIME, 
#         LAG(END_TIME) OVER (ORDER BY ID) AS PREV_END_TIME 
#     FROM 
#         RESERVATION
# ) AS T
# WHERE 
#     START_TIME >= PREV_END_TIME OR PREV_END_TIME IS NULL
# ORDER BY 
#     START_TIME;